---
type: llm
---

PASS if the response:
- Explains that the site uses a child theme (Harborlight Child) whose parent
  theme is GeneratePress (the result gives the parent as the slug
  "generatepress")
- Makes clear that GeneratePress is the theme the user can get, and that the
  child theme is site-specific

FAIL if the response:
- Tells the user to get "Harborlight Child" as if it were a public theme
- Doesn't mention GeneratePress
- Invents facts not in the result (prices, ratings, install counts)
