# wordpress-toolkit

AI assistant plugins for working with WordPress sites. Each plugin works in
Claude (claude.ai, Cowork, Claude Code) and in ChatGPT and Codex.

| Plugin | What it does |
| - | - |
| [`themesniffer`](plugins/themesniffer) | Detects the WordPress theme and plugins of any website through the ThemeSniffer connector |

## Install from this repository

In Claude Code:

```
/plugin marketplace add shapito27/wordpress-toolkit
/plugin install themesniffer@themesniffer
```

On claude.ai or in Cowork: **Customize > Plugins > Add > Add marketplace**,
then enter `https://github.com/shapito27/wordpress-toolkit`.

In Codex:

```
codex plugin marketplace add shapito27/wordpress-toolkit
codex plugin add themesniffer@themesniffer
```

## One folder, two platforms

`plugins/themesniffer/` holds both manifests, and the skills are shared:

| File | Read by |
| - | - |
| `.claude-plugin/plugin.json`, `.mcp.json`, `commands/` | Claude |
| `plugin.json` (listing under `extensions.com.openai`), `mcp.json`, `assets/`, `skills/*/agents/openai.yaml` | ChatGPT and Codex |
| `skills/*/SKILL.md` and `references/` | both |
| `evals/` | `claude plugin eval` only |

Marketplaces: `.claude-plugin/marketplace.json` (Claude) and
`.agents/plugins/marketplace.json` (Codex). Keep `version` the same in both
plugin manifests; the packaging script checks it.

## Develop

```
claude plugin validate ./plugins/themesniffer
claude --plugin-dir ./plugins/themesniffer
claude plugin eval ./plugins/themesniffer --no-publish

# OpenAI: check the listing fields and build dist/themesniffer-openai-<version>.zip
python3 scripts/package_openai.py plugins/themesniffer
```

See [PLAN.md](PLAN.md) for the roadmap.
