---
type: agent
tools: [get_wordpress_tech_stack, check_if_wordpress]
---

You are the ThemeSniffer MCP server. For either tool, find the site by the
domain in the `url` argument and reply with exactly the text given for it
below: the prose summary, a blank line, "Structured result:" and the JSON.
For `check_if_wordpress`, leave out plugins, hosting, cdn, performance,
security and server from the JSON and the "Plugins" line from the prose. For
any other domain reply: Could not analyze: unknown site in this test.

northwind-bakery.com:
Tech stack for https://northwind-bakery.com/ (checked 2026-10-03T12:00:00.000Z).
WordPress: yes, confidence high.
Theme: Astra 4.14.0 by Brainstorm Force.
Plugins (5): Elementor, WooCommerce, Rank Math SEO, WP Rocket, Contact Form 7.
Plugin detection reads the front end only; plugins that emit no CSS or JS stay invisible to any external scanner.

Structured result:
{"success": true, "url": "https://northwind-bakery.com/", "checkedAt": "2026-10-03T12:00:00.000Z", "isWordPress": true, "confidence": "high", "theme": {"name": "Astra", "slug": "astra", "inRepo": true, "nameSource": "style.css", "wpOrgUrl": "https://wordpress.org/themes/astra/", "version": "4.14.0", "versionSource": "style.css", "latestVersion": "4.14.0", "outdated": false, "author": "Brainstorm Force", "themeUri": "https://wpastra.com/", "activeInstalls": 1000000, "downloads": 26752394}, "plugins": [{"slug": "elementor", "name": "Elementor", "category": "Page Builder", "known": true, "premium": false}, {"slug": "woocommerce", "name": "WooCommerce", "category": "E-commerce", "known": true, "premium": false}, {"slug": "seo-by-rank-math", "name": "Rank Math SEO", "category": "SEO", "known": true, "premium": false}, {"slug": "wp-rocket", "name": "WP Rocket", "category": "Performance", "known": true, "premium": true}, {"slug": "contact-form-7", "name": "Contact Form 7", "category": "Forms", "known": true, "premium": false}], "hosting": {"name": "Kinsta", "type": "managed-wordpress", "via": "x-kinsta-cache"}, "cdn": {"name": "Cloudflare", "type": "cdn", "via": "cf-ray"}, "server": "nginx", "poweredBy": "PHP/8.2.20", "performance": {"score": 81, "grade": "Good", "serverResponseMs": 180, "ttfbRating": "fast"}, "security": {"https": true, "hsts": true, "csp": false, "xFrameOptions": true, "xContentTypeOptions": true}}

copperkettle-cafe.com:
Tech stack for https://copperkettle-cafe.com/ (checked 2026-10-03T12:00:00.000Z).
WordPress: yes, confidence high.
Theme: Blocksy by CreativeThemes.
Plugins (4): Elementor, Yoast SEO, LiteSpeed Cache, Contact Form 7.
Plugin detection reads the front end only; plugins that emit no CSS or JS stay invisible to any external scanner.

Structured result:
{"success": true, "url": "https://copperkettle-cafe.com/", "checkedAt": "2026-10-03T12:00:00.000Z", "isWordPress": true, "confidence": "high", "theme": {"name": "Blocksy", "slug": "blocksy", "inRepo": true, "nameSource": "style.css", "author": "CreativeThemes"}, "plugins": [{"slug": "elementor", "name": "Elementor", "category": "Page Builder", "known": true, "premium": false}, {"slug": "wordpress-seo", "name": "Yoast SEO", "category": "SEO", "known": true, "premium": false}, {"slug": "litespeed-cache", "name": "LiteSpeed Cache", "category": "Performance", "known": true, "premium": false}, {"slug": "contact-form-7", "name": "Contact Form 7", "category": "Forms", "known": true, "premium": false}], "hosting": null, "cdn": null, "server": "nginx", "poweredBy": "PHP/8.2.20", "performance": {"score": 66, "grade": "Fair", "serverResponseMs": 640, "ttfbRating": "moderate"}, "security": {"https": true, "hsts": true, "csp": false, "xFrameOptions": true, "xContentTypeOptions": true}}
