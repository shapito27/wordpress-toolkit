# ThemeSniffer - WordPress Theme & Plugin Detector

Find out which WordPress theme and plugins any website uses, right from a
conversation with Claude. The plugin connects Claude to the ThemeSniffer
service and teaches it how to read the results: it names the active theme
(and its parent theme when a child theme is used), lists detected plugins
grouped by category such as page builders, SEO, caching, e-commerce, forms and
security, and links to where you can get them.

## Use it

Ask Claude about any public website, for example:

- "What WordPress theme does example.com use?"
- "Which plugins is this site running? https://example.com"
- "Compare the WordPress stack of site-a.com and site-b.com"

In Claude Code and Cowork you can also run the commands directly:

- `/themesniffer:sniff example.com` - detect the theme and plugins of one site
- `/themesniffer:compare site-a.com site-b.com` - compare several sites

## Setup

1. Install the plugin from the Claude plugin directory (or from this
   repository's marketplace).
2. Open the plugin's **Connectors** tab and connect **ThemeSniffer**.

In Claude Code the connector loads with the plugin; run `/mcp` to check that
it is connected.

## Data

When you ask about a website, the website address you give is sent to the
ThemeSniffer service at themesniffer.com, which loads that public page and
returns the detected theme and plugins. Nothing else from your conversation is
sent. The plugin itself runs no code on your computer and stores nothing. See
the ThemeSniffer privacy policy at https://themesniffer.com for how the
service handles requests.

## Limits

- Only plugins that leave traces on the public front end of a site can be
  detected. Backend-only plugins (backups, admin tools) are invisible.
- Sites behind strict firewalls or bot protection may not be analyzable.
- Results reflect the page at the time of the check.

## Support

Questions and bug reports: https://github.com/shapito27/wordpress-toolkit/issues

## License

MIT - see [LICENSE](LICENSE).
