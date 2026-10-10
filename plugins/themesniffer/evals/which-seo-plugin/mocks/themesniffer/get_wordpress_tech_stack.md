---
expect:
  url: string
---

Tech stack for https://copperkettle-cafe.com/ (checked 2026-10-03T12:00:00.000Z).
WordPress: yes, confidence high.
Theme: Blocksy by CreativeThemes.
Plugins (4): Elementor, Yoast SEO, LiteSpeed Cache, Contact Form 7.
Plugin detection reads the front end only; plugins that emit no CSS or JS stay invisible to any external scanner.

Structured result:
{
  "success": true,
  "url": "https://copperkettle-cafe.com/",
  "checkedAt": "2026-10-03T12:00:00.000Z",
  "isWordPress": true,
  "confidence": "high",
  "theme": {
    "name": "Blocksy",
    "slug": "blocksy",
    "inRepo": true,
    "nameSource": "style.css",
    "author": "CreativeThemes",
    "wpOrgUrl": "https://wordpress.org/themes/blocksy/"
  },
  "plugins": [
    {
      "slug": "elementor",
      "name": "Elementor",
      "category": "Page Builder",
      "known": true,
      "premium": false
    },
    {
      "slug": "wordpress-seo",
      "name": "Yoast SEO",
      "category": "SEO",
      "known": true,
      "premium": false,
      "version": "23.6"
    },
    {
      "slug": "litespeed-cache",
      "name": "LiteSpeed Cache",
      "category": "Performance",
      "known": true,
      "premium": false
    },
    {
      "slug": "contact-form-7",
      "name": "Contact Form 7",
      "category": "Forms",
      "known": true,
      "premium": false
    }
  ],
  "hosting": null,
  "cdn": null,
  "server": "nginx",
  "poweredBy": "PHP/8.2.20",
  "performance": {
    "score": 81,
    "grade": "Good",
    "serverResponseMs": 180,
    "ttfbRating": "fast"
  },
  "security": {
    "https": true,
    "hsts": true,
    "csp": false,
    "xFrameOptions": true,
    "xContentTypeOptions": true
  }
}
