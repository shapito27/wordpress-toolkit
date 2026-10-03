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
2. Open the plugin's **Connectors** tab and connect **ThemeSniffer**. No
   account, sign-in or API key is needed.

In Claude Code the connector loads with the plugin; run `/mcp` to check that
it is connected.

## What the connector provides

The ThemeSniffer connector (`https://themesniffer.com/api/mcp`) offers four
tools. The skills in this plugin use the first two:

- `check_if_wordpress` - WordPress verdict, confidence and the active theme
- `get_wordpress_tech_stack` - theme, plugins, hosting, CDN, server, security
  headers and a speed snapshot
- `detect_website_fonts` - the fonts a site uses
- `extract_color_palette` - a site's color palette

The service is free and allows about 30 requests a minute per IP address.

## Data

When you ask about a website, the website address you give is sent to the
ThemeSniffer service at themesniffer.com, which fetches that public page and
returns what it detected. Nothing else from your conversation is sent. If the
ThemeSniffer connector isn't connected, Claude can instead do a best-effort
manual check by reading the public page you named (and its theme stylesheet)
with its own web tools; nothing is sent to ThemeSniffer then. The plugin
itself runs no code on your computer and stores nothing. See the ThemeSniffer
privacy policy at https://themesniffer.com/privacy for how the service handles
requests.

## Limits

- Only plugins that leave traces on the public front end of a site can be
  detected. Backend-only plugins (backups, SMTP, admin tools) are invisible,
  and sites that bundle all their CSS and JS into one file look emptier than
  they are.
- Sites behind strict firewalls or bot protection may not be analyzable. The
  plugin then says who blocked the check rather than guessing.
- Results reflect the page at the time of the check.

## Support

Plugin bugs: https://github.com/shapito27/wordpress-toolkit/issues

Detection results and the ThemeSniffer service: https://themesniffer.com/contact

## License

MIT - see [LICENSE](LICENSE).
