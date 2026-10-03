---
type: agent
expect:
  url: string
---


You are the ThemeSniffer server answering `analyze_url`. Reply with only the
JSON below for the matching site (match on the domain in `url`). For any
other domain, reply with: {"error": "unknown site in this test"}

northwind-bakery.com:
{"url": "https://northwind-bakery.com/", "is_wordpress": true,
 "theme": {"name": "Astra", "slug": "astra", "author": "Brainstorm Force", "is_child": false, "is_custom": false, "price": "free"},
 "plugins": [
  {"name": "Elementor", "slug": "elementor", "category": "page-builder"},
  {"name": "WooCommerce", "slug": "woocommerce", "category": "ecommerce"},
  {"name": "Rank Math SEO", "slug": "seo-by-rank-math", "category": "seo"},
  {"name": "WP Rocket", "slug": "wp-rocket", "category": "caching"},
  {"name": "Contact Form 7", "slug": "contact-form-7", "category": "forms"}]}

copperkettle-cafe.com:
{"url": "https://copperkettle-cafe.com/", "is_wordpress": true,
 "theme": {"name": "Blocksy", "slug": "blocksy", "author": "CreativeThemes", "is_child": false, "is_custom": false, "price": "free"},
 "plugins": [
  {"name": "Elementor", "slug": "elementor", "category": "page-builder"},
  {"name": "Yoast SEO", "slug": "wordpress-seo", "category": "seo"},
  {"name": "LiteSpeed Cache", "slug": "litespeed-cache", "category": "caching"},
  {"name": "Contact Form 7", "slug": "contact-form-7", "category": "forms"}]}
