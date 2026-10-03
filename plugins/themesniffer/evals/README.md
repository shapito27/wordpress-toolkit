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
https://themesniffer.com/api/mcp. Each case answers `check_if_wordpress` and
`get_wordpress_tech_stack` with a fixed response in
`<case>/mocks/themesniffer/`, shaped like the real server: a prose summary
followed by the structured result. As on the live server, a site that could
not be read comes back as a tool error (`error: true`) that still carries the
`blocked` / `note` data. All sites in the fixtures are fictional.
