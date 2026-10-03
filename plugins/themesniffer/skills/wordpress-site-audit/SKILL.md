---
name: wordpress-site-audit
description: Report the full WordPress stack (theme, page builder and plugins) of one or more websites and compare them. Use for competitor research, client prospecting, migration or redesign scoping, or when the user asks to compare how several sites are built.
---

# WordPress stack report and comparison

Combine theme and plugin detection into one report, and for several sites,
a side-by-side comparison.

## Steps

1. **Collect the URLs.** Normalize each one (add `https://`, drop tracking
   parameters, remove duplicates). For more than 10 sites, confirm with the
   user before running, since each site is a separate check.
2. **Detect each site** with the ThemeSniffer connector. If it offers a bulk
   tool, use it; otherwise check sites one at a time. Keep going if one site
   fails and report the failure in its row.
3. **Interpret each result** the same way as the `detect-wordpress-theme` and
   `detect-wordpress-plugins` skills (child themes, custom themes, page
   builders, not WordPress).
4. **Write the report.**

### One site

```
## <site>

**Theme:** <Theme> (<parent, if child theme>) - <free/premium/custom>
**Page builder:** <name or "none detected">
**E-commerce:** <name or "none detected">
**SEO:** <name or "none detected">

**All detected plugins** (<N>)
<grouped list as in detect-wordpress-plugins>

**Notes**
- <only observations the data supports, see below>
```

### Several sites

Start with a comparison table, one column per site:

```
| | site-a.com | site-b.com |
| - | - | - |
| WordPress | Yes | Yes |
| Theme | Astra | Custom (agency-x) |
| Page builder | Elementor | none detected |
| E-commerce | WooCommerce | - |
| SEO | Rank Math | Yoast SEO |
| Caching | WP Rocket | LiteSpeed Cache |
| Plugins detected | 14 | 9 |
```

Then:
- **Shared:** plugins every site uses.
- **Differences** that matter for the user's goal (for example different
  page builders or store platforms).
- A per-site plugin list only if the user asks, or if there are 3 sites or
  fewer.

## What to put in Notes

Only observations the data supports, such as:

- More than one plugin doing the same job (two SEO or two caching plugins).
- A page builder plus a theme that has its own builder.
- Not WordPress, or a custom theme that can't be bought.
- A version or security finding, only if the connector reported it.

Don't speculate about performance, security or traffic.

## Rules

- Never invent themes, plugins, versions or links.
- Always end with the caveat that backend-only plugins can't be detected.
- Only analyze the sites the user named.
