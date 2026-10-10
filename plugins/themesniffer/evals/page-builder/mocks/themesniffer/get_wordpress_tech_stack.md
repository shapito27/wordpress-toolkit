---
expect:
  url: string
---

Tech stack for https://velvetfox-salon.com/ (checked 2026-10-03T12:00:00.000Z).
WordPress: yes, confidence high.
Theme: Hello Elementor 3.1.1 by Elementor Team.
Plugins (2): Elementor, Elementor Pro.
Plugin detection reads the front end only; plugins that emit no CSS or JS stay invisible to any external scanner.

Structured result:
{
  "success": true,
  "url": "https://velvetfox-salon.com/",
  "checkedAt": "2026-10-03T12:00:00.000Z",
  "isWordPress": true,
  "confidence": "high",
  "theme": {
    "name": "Hello Elementor",
    "slug": "hello-elementor",
    "inRepo": true,
    "nameSource": "style.css",
    "version": "3.1.1",
    "versionSource": "style.css",
    "latestVersion": "3.1.1",
    "outdated": false,
    "author": "Elementor Team",
    "wpOrgUrl": "https://wordpress.org/themes/hello-elementor/",
    "activeInstalls": 1000000
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
      "slug": "elementor-pro",
      "name": "Elementor Pro",
      "category": "Page Builder",
      "known": true,
      "premium": true
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
