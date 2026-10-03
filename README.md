# wordpress-toolkit

Claude plugins for working with WordPress sites.

| Plugin | What it does |
| - | - |
| [`themesniffer`](plugins/themesniffer) | Detects the WordPress theme and plugins of any website through the ThemeSniffer connector |

## Install from this repository

In Claude Code:

```
/plugin marketplace add shapito27/wordpress-toolkit
/plugin install themesniffer@themesniffer
```

On claude.ai or in Cowork: **Customize > Plugins > Add > Add marketplace**,
then enter `https://github.com/shapito27/wordpress-toolkit`.

## Develop

```
claude plugin validate ./plugins/themesniffer
claude --plugin-dir ./plugins/themesniffer
```

See [PLAN.md](PLAN.md) for the roadmap.
