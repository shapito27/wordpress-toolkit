#!/usr/bin/env python3
"""Check a plugin's OpenAI listing fields and build the ZIP for the OpenAI portal.

The plugin folder serves Claude and OpenAI at once. OpenAI reads the root
plugin.json and mcp.json; Claude reads .claude-plugin/ and .mcp.json. The ZIP
for OpenAI leaves out the Claude-only parts (manifest, MCP file, commands) and
the evals, which neither directory needs.

Usage: python3 scripts/package_openai.py [plugins/themesniffer]
Writes dist/<name>-openai-<version>.zip. Exits non-zero on any problem.
"""
import json
import struct
import sys
import zipfile
from pathlib import Path

EXCLUDE_TOP = {".claude-plugin", ".mcp.json", "commands", "evals"}
EXCLUDE_NAMES = {".DS_Store", "Thumbs.db", "desktop.ini"}

# Limits from https://developers.openai.com/plugins/deploy/submission
TEXT_LIMITS = {
    "displayName": 30,
    "shortDescription": 30,
    "longDescription": 4000,
    "developerName": 80,
}
REQUIRED_INTERFACE = [
    "displayName", "shortDescription", "longDescription", "developerName",
    "category", "logo", "composerIcon",
    "websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL",
]


def png_size(path):
    data = path.read_bytes()[:24]
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return struct.unpack(">II", data[16:24])


def relative_luminance(hex_color):
    def channel(c):
        c = c / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (int(hex_color[i:i + 2], 16) for i in (1, 3, 5))
    return 0.2126 * channel(r) + 0.7152 * channel(g) + 0.0722 * channel(b)


def contrast(a, b):
    la, lb = sorted((relative_luminance(a), relative_luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def check(root):
    problems = []
    manifest = json.loads((root / "plugin.json").read_text())
    for key in ("name", "version", "description"):
        if not manifest.get(key):
            problems.append(f"plugin.json: '{key}' is required")
    if not (manifest.get("author") or {}).get("name"):
        problems.append("plugin.json: 'author.name' is required")

    openai = (manifest.get("extensions") or {}).get("com.openai") or {}
    ui = openai.get("interface") or {}
    for key in REQUIRED_INTERFACE:
        if not ui.get(key):
            problems.append(f"interface.{key} is required")
    for key, limit in TEXT_LIMITS.items():
        if len(ui.get(key, "")) > limit:
            problems.append(f"interface.{key} is {len(ui[key])} chars, limit {limit}")
    for key in ("websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"):
        if ui.get(key) and not ui[key].startswith("https://"):
            problems.append(f"interface.{key} must be https")

    prompts = ui.get("defaultPrompt", [])
    prompts = [prompts] if isinstance(prompts, str) else prompts
    if len(prompts) > 3:
        problems.append("interface.defaultPrompt allows at most 3 prompts")
    for p in prompts:
        if len(p) > 128:
            problems.append(f"defaultPrompt over 128 chars: {p[:40]}...")
        if "@" in p:
            problems.append(f"defaultPrompt must not @mention: {p[:40]}...")

    for key, against, minimum in (("brandColor", "#FFFFFF", 2), ("brandColorDark", "#212121", 2)):
        color = ui.get(key)
        if color and contrast(color, against) < minimum:
            problems.append(f"interface.{key} {color} contrast vs {against} is under {minimum}:1")

    for key in ("logo", "composerIcon", "logoDark", "composerIconDark"):
        rel = ui.get(key)
        if not rel:
            continue
        if not rel.startswith("./"):
            problems.append(f"interface.{key} must start with ./")
        path = root / rel
        if not path.is_file():
            problems.append(f"interface.{key}: {rel} not found")
            continue
        if path.stat().st_size > 5 * 1024 * 1024:
            problems.append(f"interface.{key}: {rel} is over 5 MiB")
        size = png_size(path)
        if size and (size[0] != size[1] or size[0] < 48 or size[0] > 4096):
            problems.append(f"interface.{key}: {rel} is {size[0]}x{size[1]}, must be square, 48-4096 px")

    cases = (openai.get("review") or {}).get("test_cases") or {}
    positive, negative = cases.get("positive", []), cases.get("negative", [])
    if len(positive) != 5 or len(negative) != 3:
        problems.append(f"review needs exactly 5 positive and 3 negative cases, has {len(positive)} and {len(negative)}")
    # The portal rejects anything but a non-empty string in these fields
    # (tools_triggered included: one string, not a list of tool names).
    for i, case in enumerate(positive):
        for key in ("description", "prompt", "tools_triggered", "expected_behavior"):
            if not isinstance(case.get(key), str) or not case[key].strip():
                problems.append(f"positive case {i + 1}: '{key}' must be a non-empty string")
    for i, case in enumerate(negative):
        for key in ("description", "prompt"):
            if not isinstance(case.get(key), str) or not case[key].strip():
                problems.append(f"negative case {i + 1}: '{key}' must be a non-empty string")

    mcp = json.loads((root / "mcp.json").read_text()).get("mcpServers", {})
    if len(mcp) != 1:
        problems.append(f"mcp.json should declare exactly one server, has {len(mcp)}")
    for name, server in mcp.items():
        if server.get("type") != "streamable-http":
            problems.append(f"mcp.json server '{name}' needs type streamable-http")
        if not str(server.get("url", "")).startswith("https://"):
            problems.append(f"mcp.json server '{name}' needs an https url")

    claude = json.loads((root / ".claude-plugin" / "plugin.json").read_text())
    if claude.get("version") != manifest.get("version"):
        problems.append(f"version differs: plugin.json {manifest.get('version')}, .claude-plugin {claude.get('version')}")

    for skill in sorted((root / "skills").glob("*/SKILL.md")):
        head = skill.read_text().split("---")[1] if skill.read_text().startswith("---") else ""
        if "name:" not in head or "description:" not in head:
            problems.append(f"{skill.relative_to(root)}: frontmatter needs name and description")
    return manifest, problems


def build(root, manifest):
    out_dir = root.parent.parent / "dist"
    out_dir.mkdir(exist_ok=True)
    out = out_dir / f"{manifest['name']}-openai-{manifest['version']}.zip"
    files = []
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        if not path.is_file() or rel.parts[0] in EXCLUDE_TOP or path.name in EXCLUDE_NAMES:
            continue
        files.append(rel)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for rel in files:
            zf.write(root / rel, Path(root.name) / rel)
    return out, files


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "plugins/themesniffer").resolve()
    manifest, problems = check(root)
    if problems:
        print("Problems:")
        for p in problems:
            print(f"  - {p}")
        sys.exit(1)
    out, files = build(root, manifest)
    print(f"OK: {out.relative_to(Path.cwd()) if out.is_relative_to(Path.cwd()) else out} ({len(files)} files)")
    for rel in files:
        print(f"  {rel}")


if __name__ == "__main__":
    main()
