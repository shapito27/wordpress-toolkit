---
expect:
  url: string
---

Tech stack for https://northwind-bakery.com/ (checked 2026-10-03T12:00:00.000Z).
WordPress: yes, confidence high.
Theme: Astra 4.8.1 by Brainstorm Force.
Plugins (1): Contact Form 7.
Plugin detection reads the front end only; plugins that emit no CSS or JS stay invisible to any external scanner.

Structured result:
{
  "success": true,
  "url": "https://northwind-bakery.com/",
  "checkedAt": "2026-10-03T12:00:00.000Z",
  "isWordPress": true,
  "confidence": "high",
  "theme": {
    "name": "Astra",
    "slug": "astra",
    "inRepo": true,
    "nameSource": "style.css",
    "wpOrgUrl": "https://wordpress.org/themes/astra/",
    "version": "4.8.1",
    "versionSource": "style.css",
    "latestVersion": "4.14.0",
    "outdated": true,
    "author": "Brainstorm Force",
    "themeUri": "https://wpastra.com/",
    "activeInstalls": 1000000,
    "downloads": 26752394
  },
  "plugins": [
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
