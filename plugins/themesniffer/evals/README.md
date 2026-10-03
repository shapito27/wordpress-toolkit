# ThemeSniffer plugin evals

Run from the repository root:

```
claude plugin eval ./plugins/themesniffer --no-publish
```

Quick iteration (one run per case, no baseline arm):

```
claude plugin eval ./plugins/themesniffer --runs 1 --ablation none --no-publish
```

The ThemeSniffer server is mocked so the suite is repeatable and needs no
network. `mocks/themesniffer/_tools.json` is the live `tools/list` from
https://themesniffer.com/api/mcp with each tool's `_meta` removed (the live
server marks its tools `ui.visibility: ["app"]`, which hides them from the
model). Each case answers `check_if_wordpress` and `get_wordpress_tech_stack`
with a fixed response in `<case>/mocks/themesniffer/`, shaped like the real
API: a prose summary followed by the structured result. All sites in the
fixtures are fictional.
