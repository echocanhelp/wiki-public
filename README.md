# Taiwanese American Historical Society — Wiki

[![Deploy](https://github.com/echocanhelp/wiki-public/actions/workflows/deploy.yml/badge.svg)](https://github.com/echocanhelp/wiki-public/actions/workflows/deploy.yml)

## 📖 About

The **Taiwanese American Historical Society (TAHS)** wiki is a living knowledge base documenting the history, culture, people, and organizations of the Taiwanese American community.

**Live site**: https://echocanhelp.github.io/wiki-public

## 🏗️ Structure

The wiki uses [Quartz 4](https://github.com/jackyzha0/quartz) and is organized by content type:

| Directory | Content |
|-----------|---------|
| `person/` | Taiwanese American individuals |
| `organization/` | Churches, associations, nonprofits |
| `location/` | Geographic areas, neighborhoods |
| `event/` | Historical events, holidays |
| `award/` | Recognitions and prizes |
| `publication/` | Books, newspapers, media |

## 📝 Contributing

### Creating a New Page

1. Choose the appropriate directory
2. Create a markdown file with the naming convention: `English-Name-中文名稱.md`
3. Include frontmatter with title, description, slug, and tags
4. Use wiki links with path prefixes: `[[person/Name-名稱]]`
5. Include both Chinese characters and romanized forms for all Chinese names

### Wiki Link Format

```markdown
[[person/Michelle-Wu-吳弭|Michelle Wu (吳弭)]]
[[organization/Good-Shepherd-Taiwanese-Presbyterian-Church|Good Shepherd TPC]]
[[location/San-Gabriel-Valley-聖蓋博谷|San Gabriel Valley]]
```

### Naming Conventions

- **Files**: Lowercase hyphenated slugs with Chinese characters
- **Links**: Always include path prefixes (`person/`, `organization/`, etc.)
- **Chinese names**: MUST include both 漢字 and romanized forms

## 🚀 Deployment

Pushes to `master` trigger automatic builds and deployment to GitHub Pages.

**CI/CD**:
- Node.js 22 with npm caching
- Quartz 4 build pipeline
- GitHub Pages hosting

## 📚 Documentation

For detailed wiki conventions, audit procedures, and maintenance guides:
→ [Wiki Guide](docs/wiki-guide.md)

## 📄 License

This project is maintained by the Taiwanese American Historical Society.
