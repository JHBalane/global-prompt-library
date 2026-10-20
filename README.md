# Global Prompt Library

Community-driven collection of AI prompts for productivity, development, and creativity.

## Features

- 🎯 **Curated prompts** - High-quality prompts tested by the community
- 🌍 **Multi-language support** - Prompts in multiple languages
- 📱 **Cross-platform** - Works with all major AI models
- 🔄 **Version controlled** - Track changes and improvements
- 📖 **Well documented** - Each prompt includes examples and variables

## Quick Start

Browse and download prompts directly in TextDeck, or clone this repository to contribute.

## Repository Structure

```
├── packs/
│   ├── official/          # Official TextDeck prompt packs
│   └── community/         # Community-contributed packs
├── enrichment/            # Per-pack extras: use case, worked example, translations
├── catalog/
│   └── index.json         # Auto-generated catalog index
└── .github/
    └── workflows/         # Automated validation
```

## Building

```
python3 scripts/make-packs.py          # authoring/*.py -> packs/official/
python3 scripts/apply-enrichment.py    # enrichment/*.json -> into the packs
python3 scripts/build-index.py         # catalog/index.json
```

`enrichment/<pack-id>.json` adds, per prompt, a use case, why it works, one worked
example (input and output) and full translations (title, description, prompt,
variable labels, example). Translations must use exactly the original prompt's
`{{variables}}`; the script refuses anything else.

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on submitting new prompts.

## License

This project is licensed under the TextDeck Community License - see [LICENSE](LICENSE) for details.

