---
type: llm
---

PASS if the response:
- Says the site couldn't be analyzed because it blocked the check (firewall,
  bot protection or a 403)
- Offers a next step, such as a manual check of the page source or trying again
  later

FAIL if the response:
- Names a theme or any plugins for the site
- Pretends the analysis succeeded
