---
expect:
  url: string
---

Tech stack for https://greenleaf-nursery.com/ (checked 2026-10-03T12:00:00.000Z).
WordPress: yes, confidence high.
Theme: Kadence 1.2.9 by KadenceWP.
Plugins (8): WooCommerce, Kadence Blocks, Rank Math SEO, WP Rocket, WPForms Lite, Google Analytics For Wordpress, Complianz Gdpr, Instagram Feed.
Plugin detection reads the front end only; plugins that emit no CSS or JS stay invisible to any external scanner.

Structured result:
{
  "success": true,
  "url": "https://greenleaf-nursery.com/",
  "checkedAt": "2026-10-03T12:00:00.000Z",
  "isWordPress": true,
  "confidence": "high",
  "theme": {
    "name": "Kadence",
    "slug": "kadence",
    "inRepo": true,
    "nameSource": "style.css",
    "version": "1.2.9",
    "versionSource": "style.css",
    "latestVersion": "1.2.9",
    "outdated": false,
    "author": "KadenceWP",
    "wpOrgUrl": "https://wordpress.org/themes/kadence/",
    "activeInstalls": 300000
  },
  "plugins": [
    {
      "slug": "woocommerce",
      "name": "WooCommerce",
      "category": "E-commerce",
      "known": true,
      "premium": false,
      "version": "9.3.3"
    },
    {
      "slug": "kadence-blocks",
      "name": "Kadence Blocks",
      "category": "Page Builder",
      "known": true,
      "premium": false
    },
    {
      "slug": "seo-by-rank-math",
      "name": "Rank Math SEO",
      "category": "SEO",
      "known": true,
      "premium": false
    },
    {
      "slug": "wp-rocket",
      "name": "WP Rocket",
      "category": "Performance",
      "known": true,
      "premium": true
    },
    {
      "slug": "wpforms-lite",
      "name": "WPForms Lite",
      "category": "Forms",
      "known": true,
      "premium": false
    },
    {
      "slug": "google-analytics-for-wordpress",
      "name": "Google Analytics For Wordpress",
      "category": "Other",
      "known": false,
      "premium": false
    },
    {
      "slug": "complianz-gdpr",
      "name": "Complianz Gdpr",
      "category": "Other",
      "known": false,
      "premium": false
    },
    {
      "slug": "instagram-feed",
      "name": "Instagram Feed",
      "category": "Other",
      "known": false,
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
