---
name: detect-wordpress-plugins
description: List the WordPress plugins a website uses. Use when the user asks which plugins a site runs, or which page builder, SEO, caching, forms, e-commerce, membership or multilingual plugin it uses, or wants to add the same features to their own site.
---

# Detect a website's WordPress plugins

Use the ThemeSniffer connector to find the plugins a site uses, group them so
they're easy to scan, and be clear about what can't be detected.

## Steps

1. **Get the URL** the same way as for theme detection: accept bare domains,
   add `https://`, drop tracking parameters, one site per check.
2. **Run the detection.** Call the ThemeSniffer connector's tool that analyzes
   a URL. It usually returns the theme as well; include it in one line at the
   top of the answer. If the connector offers a plugin details lookup, use it
   only for plugins the user asks about or when the result lacks a name.
3. **Group the plugins** by category using the category from the result. When
   the result has none, use `references/plugin-categories.md`. Put anything
   unmatched under "Other". Don't guess a category from the name alone if
   you're unsure; use "Other".
4. **Answer** in this shape:

   ```
   **<site>** runs WordPress with the <Theme> theme and <N> detected plugins.

   **Page builder**
   - <Plugin name> - <free/premium if known> - <link>

   **SEO**
   - ...

   Note: only plugins that leave traces on the public pages can be detected.
   Backend-only plugins (backups, security scanners, admin tools) won't show up.
   ```

   - Order categories by how useful they are for rebuilding the site: page
     builder, e-commerce, SEO, forms, caching/performance, then the rest.
   - Show a version only if the result reports one, and don't present it as
     certain.
   - If the user asked about one kind of plugin ("which SEO plugin?"), answer
     that first in one line, then offer the full list.
5. **Add the caveat** about undetectable plugins every time. If no plugins
   were found, say that this doesn't mean the site has none.

## Rules

- Never invent plugins, versions, prices or links. Report only what the
  connector returned or what you saw on the page yourself.
- Don't paste raw tool output.
- Don't make security claims (for example "this version is vulnerable")
  unless the connector's result says so.
- Only analyze sites the user asked about.

## If the connector isn't available

Tell the user that connecting ThemeSniffer from the plugin's Connectors tab
gives the most complete result. If you can fetch web pages, look for
`/wp-content/plugins/<slug>/` in the page's asset URLs, plugin HTML comments
and generator meta tags, map slugs with `references/plugin-categories.md`, and
label the answer as a manual check.
