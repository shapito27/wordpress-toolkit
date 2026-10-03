---
expect:
  url: string
---

Tech stack for https://harborlight-dental.com/ (checked 2026-10-03T12:00:00.000Z).
WordPress: yes, confidence high.
Theme: Harborlight Child 1.0.0 by Harborlight Dental.
Plugins (1): Gp Premium.
Plugin detection reads the front end only; plugins that emit no CSS or JS stay invisible to any external scanner.

Structured result:
{
  "success": true,
  "url": "https://harborlight-dental.com/",
  "checkedAt": "2026-10-03T12:00:00.000Z",
  "isWordPress": true,
  "confidence": "high",
  "theme": {
    "name": "Harborlight Child",
    "slug": "harborlight-child",
    "inRepo": false,
    "nameSource": "style.css",
    "version": "1.0.0",
    "versionSource": "style.css",
    "author": "Harborlight Dental",
    "parentTheme": "generatepress",
    "themeUri": "https://harborlight-dental.com/"
  },
  "plugins": [
    {
      "slug": "gp-premium",
      "name": "Gp Premium",
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
