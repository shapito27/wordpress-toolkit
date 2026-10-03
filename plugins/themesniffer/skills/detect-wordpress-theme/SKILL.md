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
2. **Run the detection.** Call the ThemeSniffer connector's tool that analyzes
   a URL. If the connector also offers a theme details lookup and the result
   lacks the author, price or download link, look the theme up by its slug.
3. **Interpret the result.**
   - **Child theme:** name both. The child theme is usually site-specific; the
     parent theme is what the user can download or buy. Lead with the parent.
   - **Custom or renamed theme:** say the theme looks bespoke or renamed and
     can't be bought as-is. If the result names a parent or a framework (for
     example Genesis, Underscores, Sage), say the site was built on it.
   - **Block theme / site editor:** mention it when the result says so, since
     it changes how the design is customized.
   - **Page builder in use** (Elementor, Divi, Beaver Builder, Bricks and
     similar): say that much of the look comes from the builder, not the
     theme, so installing the theme alone won't reproduce the design.
   - **Not WordPress:** say so plainly and name the platform if the result
     gives one. Don't guess a theme.
   - **Couldn't analyze** (blocked, timeout, error): say what happened in one
     line, then offer the manual check below.
4. **Answer** in the format in `references/output-format.md`.

## Rules

- Never invent a theme name, author, version, price or link. Report only what
  the connector returned or what you saw on the page yourself. If something is
  unknown, say "unknown".
- Don't paste raw tool output. Summarize it.
- Prefer links the connector returned. Otherwise link the wordpress.org theme
  page (`https://wordpress.org/themes/<slug>/`) only when the result says the
  theme is listed there.
- Only analyze sites the user asked about. Don't crawl beyond the pages needed.
- If the user also wants the plugins, follow the `detect-wordpress-plugins`
  skill in the same answer.

## If the connector isn't available

If the ThemeSniffer tools aren't connected, tell the user that connecting
ThemeSniffer from the plugin's Connectors tab gives the most reliable result.
If you can fetch web pages, you can do a best-effort manual check with
`references/manual-detection.md`, and label the answer as a manual check.
