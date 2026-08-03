// Quartz config
import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

const config: QuartzConfig = {
  configuration: {
    pageTitle: "Echopedia",
    pageTitleSuffix: "",
    enableSPA: false,
    enablePopovers: true,
    analytics: {
      provider: "plausible",
    },
    locale: "en-US",
    baseUrl: "echocanhelp.github.io/wiki-public",
    ignorePatterns: ["private", "templates", ".obsidian", "articles/**"],
    defaultDateType: "created",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Schibsted Grotesk",
        body: "Source Sans Pro",
        code: "IBM Plex Mono",
      },
      colors: {
        lightMode: {
          light: "#faf8f8",
          lightgray: "#e5e5e5",
          gray: "#b8b8b8",
          darkgray: "#4e4e4e",
          dark: "#2b2b2b",
          secondary: "#284b63",
          tertiary: "#84a59d",
          highlight: "rgba(143, 159, 169, 0.15)",
          textHighlight: "#fff23688",
        },
        darkMode: {
          light: "#161618",
          lightgray: "#393639",
          gray: "#646464",
          darkgray: "#d4d4d4",
          dark: "#ebebec",
          secondary: "#7b97aa",
          tertiary: "#84a59d",
          highlight: "rgba(143, 159, 169, 0.15)",
          textHighlight: "#fff23688",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.ObsidianFlavoredMarkdown(),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.CrawlLinks(),
      Plugin.Description(),
      Plugin.TableOfContents(),
      Plugin.CreatedModifiedDate(),
    ],
    filters: [],
    emitters: [
      Plugin.Assets(),
      Plugin.ContentPage({
        routeStart: "/",
        renderToc: false,
      }),
      // FolderPage emits people/index.html + organizations/index.html with full site chrome.
      // ContentPage intentionally skips */index.md; without this, directory URLs need a post-build hack.
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        emitAs: "json",
        sort: (f1, f2) => f1.title.localeCompare(f2.title),
      }),
      Plugin.CNAME(),
      Plugin.Favicon(),
      Plugin.ComponentResources(),
      Plugin.NotFoundPage(),
    ],
  },
}

export default config
