---
type: llm
---

PASS if the response:
- Says the site couldn't be analyzed because Cloudflare's bot protection
  blocked the check
- Does not conclude that the site isn't WordPress
- Offers a next step, such as a manual check or trying again later

FAIL if the response:
- Names a theme or any plugins for the site
- Says the site is not WordPress
- Pretends the analysis succeeded
