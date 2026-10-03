# ThemeSniffer plugin evals

Run from the repository root:

```
claude plugin eval ./plugins/themesniffer --no-publish
```

Quick iteration (one run per case, no baseline arm):

```
claude plugin eval ./plugins/themesniffer --runs 1 --ablation none --no-publish
```

The ThemeSniffer server is mocked: `mocks/themesniffer/_tools.json` declares
an assumed `analyze_url(url)` tool, and each case answers it with a fixed
response in `<case>/mocks/themesniffer/analyze_url.md`. All sites in the
fixtures are fictional. Update the tool name and response shape once the real
ThemeSniffer MCP schema is confirmed.
