---
expect:
  url: string
---

Could not analyze https://ironpeak-gym.com/: Cloudflare, which fronts this site, blocked our request (HTTP 403), so we could not check it for WordPress. That is a bot-protection rule, not an outage - the site itself is up and serves normal browsers.

Structured result:
{
  "success": true,
  "url": "https://ironpeak-gym.com/",
  "checkedAt": "2026-10-03T12:00:00.000Z",
  "isWordPress": null,
  "confidence": "unknown",
  "blocked": true,
  "blockedBy": "Cloudflare",
  "status": 403,
  "reason": "bot-protection",
  "note": "Cloudflare, which fronts this site, blocked our request (HTTP 403), so we could not check it for WordPress. That is a bot-protection rule, not an outage - the site itself is up and serves normal browsers.",
  "signalCount": 0
}
