---
name: detect-wordpress-theme
description: Identify the WordPress theme a website uses. Use when the user asks what theme a site runs, "what WordPress theme is this", whether a site is built on WordPress, wants a site's look for their own site, or shares a URL and asks how it was built or designed.
---

# Detect a website's WordPress theme

Use the ThemeSniffer connector to find which theme a site runs, then explain
the result so the user knows exactly what they can get and how.

## Steps

1. **Get the URL.** If the user named a site without a URL, ask for it. Accept
   bare domains (`example.com`) and add `https://`. Drop tracking parameters
   such as `utm_*`. Keep a path only if the user asked about that specific
   page. One site per check; for several sites, check each one.
2. **Run the detection** with the ThemeSniffer connector:
   - Theme-only question: `check_if_wordpress` (lighter, returns the theme).
   - The user also wants plugins, the page builder or "how it's built":
     `get_wordpress_tech_stack` (theme plus plugins, hosting, CDN, speed).
   Pass the URL as `url`; a bare domain is fine. Don't call both for the same
   site: the tech stack result already contains everything the WordPress
   check does.
3. **Read the result.** Each tool returns a short prose summary plus the full
   data. Key fields:
   - `isWordPress`: `true`, `false`, or `null`. **`null` means the page could
     not be read, not "not WordPress".** Check `blocked`, `blockedBy` and
     `note` and report that instead of a verdict.
   - `confidence`: high, medium, low or none. Mention it when it isn't high.
   - `theme.name` and `theme.nameSource`: when `nameSource` is `slug` the name
     was inferred from the folder name, so say it's a best guess.
   - `theme.parentTheme`: present for a child theme. It's the parent's slug.
   - `theme.inRepo` and `theme.wpOrgUrl`: free theme in the WordPress.org
     directory. `inRepo: false` means premium or custom; `theme.themeUri`
     usually shows which (a vendor's site vs. the site itself or an agency).
   - `theme.version`, `theme.latestVersion`, `theme.outdated`: mention an
     outdated theme in one line.
   - `theme.activeInstalls`: a bucketed floor, so write `500000` as
     "500,000+". `downloads` is lifetime downloads, not usage; don't present
     it as the number of sites.
   - A tool result with `isError` is a failed check. Say what the message says.
4. **Interpret it.**
   - **Child theme:** name both. The child theme is usually site-specific; the
     parent theme is what the user can download or buy. Lead with the parent.
   - **Not in the directory:** if `themeUri` points to a theme vendor, it's
     likely a premium theme from that vendor. If it points to the site itself
     or an agency, or there's no `themeUri`, it's likely custom and can't be
     bought as-is. Say how sure you are.
   - **Page builder in use** (Elementor, Divi, Beaver Builder, Bricks, Spectra
     and similar, visible in the plugins): say that much of the look comes
     from the builder, not the theme, so installing the theme alone won't
     reproduce the design.
   - **Not WordPress** (`isWordPress: false`): say so plainly. Don't guess a
     theme, and don't name another platform unless the result shows it.
   - **Couldn't analyze** (`isWordPress: null`, `blocked`, or an error): say
     what happened in one line, using `note` and `blockedBy`, then offer the
     manual check below or trying again later.
5. **Answer** in the format in `references/output-format.md`.

## Rules

- Never invent a theme name, author, version, price or link. Report only what
  the connector returned or what you saw on the page yourself. If something is
  unknown, say "unknown".
- Don't paste raw tool output. Summarize it.
- Prefer links the connector returned (`wpOrgUrl`, `themeUri`). Link a
  wordpress.org page only when `inRepo` is true.
- The connector allows about 30 requests a minute. For many sites, check them
  one at a time and don't repeat a site you already checked.
- Only analyze sites the user asked about. Don't crawl beyond the pages needed.
- If the user also wants the plugins, follow the `detect-wordpress-plugins`
  skill in the same answer.

## If the connector isn't available

If the ThemeSniffer tools aren't connected, tell the user that connecting
ThemeSniffer from the plugin's Connectors tab gives the most reliable result.
If you can fetch web pages, you can do a best-effort manual check with
`references/manual-detection.md`, and label the answer as a manual check.
