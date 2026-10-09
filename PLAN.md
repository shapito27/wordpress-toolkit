# ThemeSniffer plugin for Claude - plan

Goal: publish a Claude plugin in Anthropic's plugin directory that pairs the
ThemeSniffer MCP server (https://themesniffer.com/developers) with skills that
teach Claude how to detect a website's WordPress theme and plugins and report
the result well.

Sources used:
- https://claude.com/docs/plugins/submit
- https://claude.com/docs/plugins/pre-submission-checklist
- https://claude.com/docs/plugins/build

> Note: themesniffer.com could not be fetched from the planning environment, so
> the MCP tool names below are placeholders. See "Open questions".

---

## 1. What we ship

| Piece | Purpose | Loads in |
| - | - | - |
| `.mcp.json` | Points at the remote ThemeSniffer MCP server by URL | chat, Cowork, Claude Code |
| Skills | Tell Claude *when* and *how* to use the tools and how to present results | everywhere |
| Commands | Quick entry points: `/themesniffer:sniff`, `/themesniffer:compare` | Cowork, Claude Code (load as skills in chat) |
| README + LICENSE | Required to publish | directory |

No hooks, no local scripts, no `bin/`, no package launchers. The plugin is only
Markdown + JSON. This keeps us clear of almost every "held for a reviewer"
finding in the checklist (pinned npx/uvx, lockfiles, scripts the validator
can't follow, binaries).

## 2. Repository layout

The repo doubles as a self-hosted marketplace (so people can test before the
directory listing goes live) and holds one plugin folder that we submit.

```
wordpress-toolkit/
├── .claude-plugin/
│   └── marketplace.json          # self-hosted marketplace, lists ./plugins/themesniffer
├── plugins/
│   └── themesniffer/             # <- "Plugin path" in the developer portal
│       ├── .claude-plugin/
│       │   └── plugin.json
│       ├── .mcp.json
│       ├── README.md             # >= 40 words outside code blocks, incl. data disclosure
│       ├── LICENSE               # MIT (or set "license" in plugin.json)
│       ├── skills/
│       │   ├── detect-wordpress-theme/
│       │   │   ├── SKILL.md
│       │   │   └── references/
│       │   │       ├── output-format.md
│       │   │       └── manual-detection.md
│       │   ├── detect-wordpress-plugins/
│       │   │   ├── SKILL.md
│       │   │   └── references/
│       │   │       └── plugin-categories.md
│       │   └── wordpress-site-audit/
│       │       └── SKILL.md
│       └── commands/
│           ├── sniff.md
│           └── compare.md
├── evals/                        # claude plugin eval cases (outside plugin folder)
└── PLAN.md
```

A subfolder plugin path is fine here because we run no scripts (the subfolder
rules only hold scripts/hooks/MCP commands). Submit each plugin folder on its
own if we add more plugins later.

Checklist hygiene: no `.DS_Store`/`Thumbs.db`, no symlinks/submodules/LFS, no
`export-ignore`/`filter` in `.gitattributes`, every file < 256 KiB, folder
names `[A-Za-z0-9._-]` only.

## 3. Naming and branding

- `name`: **`themesniffer`** - permanent, lowercase, distinctive, ours.
  Becomes the command prefix (`/themesniffer:sniff`).
- `displayName`: "ThemeSniffer - WordPress Theme & Plugin Detector".
- `author.name`: the ThemeSniffer owner / company, with `url`
  `https://themesniffer.com`.
- Avoid "WordPress" as the plugin `name`: it is a trademark of the WordPress
  Foundation and the directory holds names that match a well-known brand that
  isn't ours ("Name matches a known brand"). Using it descriptively in
  `displayName`/`description` is normal ("for WordPress"). The repo name
  `wordpress-toolkit` is not shown in the listing, so it can stay.
- Submit from the Claude organization that clearly owns ThemeSniffer, so the
  reviewer can see the brand is ours.

## 4. Manifest (draft)

```json
{
  "name": "themesniffer",
  "displayName": "ThemeSniffer - WordPress Theme & Plugin Detector",
  "version": "0.1.0",
  "description": "Find out which WordPress theme and plugins any website uses. Detects child/parent themes, page builders, SEO, cache, e-commerce and security plugins through the ThemeSniffer connector.",
  "author": { "name": "ThemeSniffer", "url": "https://themesniffer.com" },
  "homepage": "https://themesniffer.com/developers",
  "repository": "https://github.com/shapito27/wordpress-toolkit",
  "license": "MIT",
  "keywords": ["wordpress", "theme-detector", "plugin-detector", "competitor-research", "seo"]
}
```

Raise `version` on every release (the directory follows the tracked branch).

## 5. MCP connection and auth - the key decision

`.mcp.json`:

```json
{
  "mcpServers": {
    "themesniffer": {
      "type": "http",
      "url": "https://themesniffer.com/api/mcp"
    }
  }
}
```

Rules from the checklist: `type` must be `http`/`sse`/`ws`, URL must be
absolute `https://`, **no secrets in the file** (blocks as "Secret in MCP
headers"), never read env vars like `$THEMESNIFFER_API_KEY` (held).

How auth works per surface:

| Server auth | claude.ai / Cowork | Claude Code |
| - | - | - |
| None (free tier, rate limited by IP) | works | works |
| **OAuth 2.1 (MCP auth spec)** | works - user connects from the plugin's Connectors tab | works |
| API key only | **does not work** - no place to enter it | works via `userConfig` (`sensitive: true`) + `"headers": {"Authorization": "Bearer ${user_config.api_key}"}` |

Recommendation: the server should support **OAuth** (best: free tier on sign-in,
paid plans unlock bulk/history) or an **authless free tier**. API-key-only
would make the plugin Claude Code-only in practice.

Also submit the server itself as an **MCP connector** in the developer portal
(separate submission). Use the exact same URL in `.mcp.json` so users who have
both see one set of tools.

Server-side requirements to verify before submitting:
- Streamable HTTP transport (preferred) at a stable `/mcp` path.
- Tool annotations: all detection tools are `readOnlyHint: true`.
- Clear, short tool descriptions and typed input schemas.
- Errors that Claude can act on: "not a WordPress site", "site blocked our
  crawler / WAF", "timeout", "rate limit, retry after N s", "quota exceeded".
- Response size kept small (structured JSON, not raw HTML).

Confirmed tools (from https://themesniffer.com/developers and the live
`tools/list`; all take `url`, a bare domain is fine):

| Tool | Returns |
| - | - |
| `check_if_wordpress` | isWordPress (true/false/null), confidence, 8 signals, theme |
| `get_wordpress_tech_stack` | the above plus plugins[] {slug, name, category, known, premium, version}, hosting, cdn, server, performance, security |
| `detect_website_fonts` | font families, providers, type scale |
| `extract_color_palette` | palette, roles, theme.json colors, contrast |

Theme fields: name, slug, nameSource (style.css / wordpress.org / slug =
guess), parentTheme (child themes), inRepo, wpOrgUrl, themeUri, version,
latestVersion, outdated, author, activeInstalls (bucketed floor), downloads.
A blocked site returns success with `isWordPress: null`, `blocked`,
`blockedBy`, `note`; a failed call is a tool result with `isError: true`.

**Server blocker (found in live testing, fixed in
shapito27/wordpress-theme-detector-landing#62, live 2026-10-03):** every tool
declared `_meta.ui.visibility: ["app"]`. Under MCP Apps that means app-only, so Claude
Code connects but hides all four tools from the model ("kept from the model")
and the skills fall back to manual checks. Fix on the server: set
`"visibility": ["model", "app"]` or drop `visibility` (the default is both).

## 6. Skills

Skill descriptions decide when Claude loads them, so they are written as user
situations, not summaries.

### 6.1 `detect-wordpress-theme`

Description: *"Identify the WordPress theme a website uses. Use when the user
asks what theme a site runs, 'what WordPress theme is this', wants to copy a
site's look, or shares a URL and asks how it was built."*

Body (workflow):
1. Normalize input: accept bare domains, add `https://`, strip tracking params;
   one URL per call.
2. Call the ThemeSniffer tool.
3. Interpret:
   - Child theme -> name both child and parent; the parent is what the user
     can buy/download.
   - Custom/unknown theme -> say it's bespoke, suggest closest commercial
     alternatives only if the tool returns them; don't invent.
   - Not WordPress -> say so plainly and name the platform if returned.
   - Blocked/timeout -> explain, offer manual detection (6.4).
4. Present per `references/output-format.md`: theme card (name, author,
   version, free/premium, link), short "how to get it", confidence note.
5. Never fabricate a theme name; if the tool returns nothing, say so.

`references/manual-detection.md` - fallback when the connector is not
connected, but web fetch is available: look for
`/wp-content/themes/<slug>/style.css` and its header (`Theme Name`,
`Template` = parent), `<meta name="generator">`, `/wp-json/` presence,
`/wp-content/plugins/<slug>/` asset paths, body classes. Always state that the
result is a best-effort manual read and recommend connecting ThemeSniffer.

### 6.2 `detect-wordpress-plugins`

Description: *"List the WordPress plugins a site uses. Use when the user asks
which plugins, page builder, SEO plugin, cache, form or e-commerce plugin a
site uses, or wants to replicate a site's features."*

Workflow: call tool -> group by category from
`references/plugin-categories.md` (page builder, SEO, caching/performance,
e-commerce, forms, security, analytics, multilingual, membership, other) ->
table with name, category, free/premium, link. Always add the caveat that only
plugins leaving front-end traces are detectable (backend-only plugins like
backups or admin tools are invisible).

### 6.3 `wordpress-site-audit`

Description: *"Give a full WordPress stack report for one or more sites. Use
for competitor research, client prospecting, migration scoping, or 'compare
these sites'."*

Combines theme + plugins into one report; for several URLs builds a
comparison table (shared plugins, differing builders). Flags only what the data
supports (e.g. "two SEO plugins detected", "outdated version reported by the
tool"); no speculative security claims.

### 6.4 Shared rules (in every SKILL.md)

- Only analyze public URLs the user provided; no crawling beyond the page.
- Don't paste raw tool JSON; summarize.
- Link to wordpress.org or the vendor page returned by the tool.
- Be explicit about confidence and detection limits.

## 7. Commands

- `commands/sniff.md` - `description: Detect the WordPress theme and plugins of a URL`. Runs 6.1 + 6.2 on `$ARGUMENTS`.
- `commands/compare.md` - `description: Compare the WordPress stack of several URLs`. Runs 6.3.

## 8. README (listing text) outline

1. One-line value: what it detects.
2. Use it: example prompts ("What theme does example.com use?",
   `/themesniffer:sniff example.com`, compare).
3. Setup: connect the ThemeSniffer connector from the plugin's Connectors tab
   (sign-in / free tier / plans).
4. **Data**: the URLs you ask about are sent to themesniffer.com; what
   ThemeSniffer stores and for how long; link to privacy policy. Nothing else
   is sent; the plugin runs no local code.
5. Limits: backend-only plugins invisible, sites behind WAF may fail.
6. Support contact.

The security scan fails plugins that send data to undisclosed destinations, so
section 4 must match exactly what the server does.

## 9. Testing

1. `claude plugin validate ./plugins/themesniffer` -> `✔ Validation passed`.
2. Claude Code: `claude --plugin-dir ./plugins/themesniffer`, check `/mcp`
   and `/themesniffer:sniff`.
3. claude.ai + Cowork: zip `plugins/themesniffer`, upload via
   Customize > Plugins > Add > Upload plugin, connect the connector, run the
   prompts.
4. Evals with `claude plugin eval` in `evals/`, comparing with and without
   the plugin. Case set:
   - known theme (e.g. a site on Astra / GeneratePress / Divi / Kadence)
   - child theme site
   - custom theme site
   - WooCommerce store
   - Elementor site
   - non-WordPress sites (Shopify, Wix, static)
   - unreachable / WAF-blocked site
   - multi-URL compare
   - bare domain input, URL with path and query
   Grade: correct theme/parent, no fabricated names, caveats present, concise.

## 10. Submission steps

1. Repo can stay private while validating (needs Claude GitHub App installed
   and source-upload consent); must be **public** before going live.
2. Connect GitHub on claude.ai in the submitting org (needs push access).
3. claude.ai/directory/manage -> Submit new -> **Plugin bundle**.
   - Repository `shapito27/wordpress-toolkit`
   - Plugin path `plugins/themesniffer`
   - Branch: `main` (or a `release` branch/tag if we want controlled releases)
4. Validate, fix Blocking findings, re-validate (results are per commit).
5. Data handling answers: reads URLs only, no personal data; data goes only to
   the declared connector (themesniffer.com); retention per ThemeSniffer
   policy; not aimed at under-18s.
6. Compliance: contact email, 4 acknowledgements.
7. Choose GitHub push webhook for updates; decide auto-publish.
8. Separately: Submit new -> **MCP connector** for the ThemeSniffer server.
9. Withdraw/delist if needed: draft -> Delete draft; in review -> Withdraw
   submission; live -> menu -> Delist plugin (Relist plugin to restore).
   Limit: 10 submissions per org per 24h, withdrawn ones count.

## 11. Milestones

| # | Milestone | Done when |
| - | - | - |
| 0 | Confirm MCP details (open questions) | tool list, auth, endpoint known - **done; server visibility fixed and live** |
| 1 | Scaffold plugin + marketplace.json, README, LICENSE | `claude plugin validate` passes - **done** |
| 2 | Write 3 skills + references + 2 commands | works in Claude Code against live MCP - **done: live runs call the real tools and load the skills** |
| 3 | Evals + iterate on skill wording | plugin beats baseline on the case set - **done against mocked server: 9 cases, with-plugin 0.99 -> 1.00 after fix, mean delta vs no plugin +0.71; re-run against the live server once its schema is known** |
| 4 | Test on claude.ai and Cowork via zip upload | all components load, connector connects |
| 5 | Portal validate (private repo), fix findings | no Blocking findings |
| 6 | Submit plugin + MCP connector, make repo public, publish | listing live |
| 7 | Post-launch: usage tab, version bumps via tracked branch | ongoing |

Later ideas (v2): bulk CSV detection, "find sites using theme X" (if the API
supports reverse lookup), outdated-version alerts, Shopify detection.

## 12. Open questions

1. ~~Endpoint/transport~~ `https://themesniffer.com/api/mcp`, Streamable HTTP,
   stateless.
2. ~~Auth~~ None, so the connector works on claude.ai, Cowork and Claude Code.
3. ~~Tool names and responses~~ See section 5.
4. ~~Rate limits~~ 30 JSON-RPC requests/min per IP on `/api/mcp`; free.
5. What ThemeSniffer logs/stores per request and retention (for the
   data-handling answers) - check https://themesniffer.com/privacy.
6. Is the submitting Claude org the ThemeSniffer owner? (brand check)
7. ~~License: MIT ok?~~ Yes, MIT.
8. Copyright holder name for LICENSE (currently "ThemeSniffer").

## 13. OpenAI (ChatGPT and Codex)

Same plugin folder, second manifest. OpenAI reads the root `plugin.json`
(Agent Plugins format) and `mcp.json` (`"type": "streamable-http"`); Claude
keeps reading `.claude-plugin/` and `.mcp.json`. Skills are shared; each has
`agents/openai.yaml` declaring its dependency on the ThemeSniffer server.
Commands are Claude-only (OpenAI asks for commands to become skills; ours only
call the existing skills, so they are left out of the OpenAI package).

- Listing: `extensions.com.openai.interface` in `plugin.json`. Developer name
  Ruslan Saifullin, category Developer Tools, icons in `assets/` (the site's
  192px icon), brand color #059669 / #10B981.
- Review: `extensions.com.openai.review.test_cases` has the 5 positive and 3
  negative cases OpenAI requires, using real sites checked against the live
  server (wpastra.com, elementor.com, generatepress.com, shopify.com).
- Package: `python3 scripts/package_openai.py plugins/themesniffer` checks the
  listing limits and writes `dist/themesniffer-openai-<version>.zip` without
  `.claude-plugin/`, `.mcp.json`, `commands/` or `evals/`.
- Verified with Codex CLI 0.162.0: the repo marketplace installs the plugin,
  `codex mcp list` shows the ThemeSniffer server, and the model prompt lists
  all three skills.
- Server (shapito27/wordpress-theme-detector-landing#63): MCP rate limit
  300/min per IP for shared assistant IPs, empty view CSP, ChatGPT status text.

Still to do, by the owner:
1. OpenAI organization with Apps Management Write, identity verified as
   Ruslan Saifullin.
2. Portal: Create plugin > With MCP > `https://themesniffer.com/api/mcp`;
   upload the ZIP; serve the portal's token at
   `/.well-known/openai-apps-challenge` (site repo follow-up).
3. Record a demo video and add it as `demo_recording_url`.
4. Test in ChatGPT (Work chat, `@ThemeSniffer`) and the Codex app.
