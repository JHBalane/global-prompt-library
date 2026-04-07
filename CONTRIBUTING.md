# Contributing to Global Prompt Library

Welcome! We're building the world's largest open collection of AI prompts. Here's how you can help.

## 🎯 Our Mission

Democratize AI prompts by creating a community-driven library that:
- Remains free for all users
- Maintains high quality standards
- Supports multiple languages and use cases
- Credits all contributors

## 🚀 Quick Start

### 1. Choose Your Contribution Type

- 📝 **New Prompt Pack**: Create a collection of related prompts
- 🔧 **Improve Existing**: Enhance current prompts
- 🌍 **Translate**: Help localize prompts to other languages
- 📋 **Review**: Test and provide feedback on submissions

### 2. Fork & Clone

```bash
git clone https://github.com/yourusername/global-prompt-library.git
cd global-prompt-library
```

### 3. Create Your Pack

Place your pack in the appropriate directory:
- `packs/community/productivity/` - Productivity tools
- `packs/community/creative/` - Creative writing, art
- `packs/community/business/` - Business and marketing
- `packs/community/development/` - Programming and tech

### 4. Submit Pull Request

1. Create a branch: `git checkout -b add-my-pack`
2. Commit your changes: `git commit -m "Add: Marketing Email Templates"`
3. Push: `git push origin add-my-pack`
4. Create Pull Request on GitHub

## 📦 Pack Format

### Basic Structure

```json
{
  "id": "unique-pack-id",
  "name": "Human Readable Pack Name",
  "version": "1.0.0",
  "author": {
    "name": "Your Name",
    "github": "yourusername",
    "website": "https://yourwebsite.com" // optional
  },
  "description": "Brief description of the pack",
  "category": "productivity|creative|business|development",
  "language": "en|de|es|fr|it|pt|nl|pl|zh|ja",
  "license": "TextDeck-Community-1.0",
  "created": "2025-01-15",
  "updated": "2025-01-20",
  "tags": ["tag1", "tag2", "tag3"],
  "prompts": [
    // Prompt objects (see below)
  ]
}
```

### Prompt Structure

```json
{
  "id": "unique-prompt-id",
  "title": "Prompt Title",
  "description": "What this prompt does",
  "content": "The actual prompt with {{variables}}",
  "variables": [
    {
      "name": "variable_name",
      "description": "What this variable is for",
      "example": "Example value",
      "required": true
    }
  ],
  "examples": [
    {
      "input": {
        "variable_name": "Example input"
      },
      "output": "Expected output example"
    }
  ],
  "tags": ["specific", "tags"],
  "difficulty": "beginner|intermediate|advanced",
  "model_compatibility": ["gpt", "claude", "gemini", "all"]
}
```

### Example: Marketing Email Pack

```json
{
  "id": "marketing-emails",
  "name": "Marketing Email Templates",
  "version": "1.0.0",
  "author": {
    "name": "Jane Doe",
    "github": "janedoe"
  },
  "description": "Professional email templates for marketing campaigns",
  "category": "business",
  "language": "en",
  "license": "TextDeck-Community-1.0",
  "created": "2025-01-15",
  "updated": "2025-01-15",
  "tags": ["marketing", "email", "business"],
  "prompts": [
    {
      "id": "product-launch",
      "title": "Product Launch Announcement",
      "description": "Craft an engaging product launch email",
      "content": "Write a compelling product launch email for {{product_name}}. Target audience: {{target_audience}}. Key benefits: {{key_benefits}}. Include an attention-grabbing subject line and clear call-to-action.",
      "variables": [
        {
          "name": "product_name",
          "description": "The name of your product",
          "example": "TextDeck Pro",
          "required": true
        },
        {
          "name": "target_audience",
          "description": "Your target customer group",
          "example": "content creators and marketers",
          "required": true
        },
        {
          "name": "key_benefits",
          "description": "Main product benefits",
          "example": "10x faster content creation, AI-powered optimization",
          "required": true
        }
      ],
      "examples": [
        {
          "input": {
            "product_name": "TextDeck Pro",
            "target_audience": "content creators",
            "key_benefits": "10x faster prompt creation"
          },
          "output": "Subject: 🚀 TextDeck Pro is here - 10x faster prompt creation!\n\nHi there,\n\nWe're thrilled to announce TextDeck Pro..."
        }
      ],
      "tags": ["email", "product-launch", "announcement"],
      "difficulty": "beginner",
      "model_compatibility": ["all"]
    }
  ]
}
```

## ✅ Quality Guidelines

### What We Love

- **Clear and specific prompts** that produce consistent results
- **Well-documented variables** with examples
- **Tested prompts** that you've actually used
- **Original content** or proper attribution
- **Inclusive language** that works for everyone

### Pack Requirements

1. **Minimum 3 prompts** per pack
2. **Tested with at least one AI model**
3. **Clear variable descriptions** and examples
4. **Appropriate category** and tags
5. **Valid JSON format** (use our validator)

### Language Standards

- Use clear, professional language
- Avoid jargon without explanation
- Include example outputs when helpful
- Test prompts before submission

## 🌍 Internationalization

### Adding Translations

1. Copy an existing pack to appropriate language folder
2. Translate all user-facing text:
   - Pack name and description
   - Prompt titles and descriptions
   - Variable descriptions
   - Examples
3. Keep `id` fields in English for consistency
4. Test with native speakers if possible

### Language Codes

- `en` - English
- `de` - Deutsch (German)
- `es` - Español (Spanish)
- `fr` - Français (French)
- `it` - Italiano (Italian)
- `pt` - Português (Portuguese)
- `nl` - Nederlands (Dutch)
- `pl` - Polski (Polish)
- `zh` - 中文 (Chinese)
- `ja` - 日本語 (Japanese)

## 🔧 Development Tools

### Validation

Before submitting, validate your pack:

```bash
python scripts/validate-pack.py packs/community/your-category/your-pack.json
```

### Testing

Test your prompts with our tool:

```bash
python scripts/test-prompts.py packs/community/your-category/your-pack.json
```

### Local Preview

Generate local index to preview:

```bash
python scripts/build-index.py
# Opens browser with preview
```

## 📝 Pull Request Guidelines

### Title Format

- `Add: [Pack Name]` for new packs
- `Improve: [Pack Name]` for enhancements
- `Translate: [Pack Name] to [Language]` for translations
- `Fix: [Issue Description]` for bug fixes

### Description Template

```markdown
## Pack Details

- **Name**: Marketing Email Templates
- **Category**: Business
- **Language**: English
- **Prompts**: 5

## Changes

- [x] Added product launch email template
- [x] Added follow-up email template
- [x] Tested all prompts with GPT-4
- [x] Validated JSON format

## Testing

I've tested these prompts with:
- [x] GPT-4
- [ ] Claude
- [ ] Gemini

All prompts produce consistent, high-quality outputs.

## Checklist

- [x] Followed pack format specification
- [x] Validated JSON with provided tool
- [x] Tested all prompts personally
- [x] Used inclusive language
- [x] Added appropriate tags and metadata
```

## 🏆 Recognition

Contributors are credited in:

1. **Pack metadata** with direct attribution
2. **Contributors file** with stats and links
3. **Monthly highlights** on social media
4. **Annual report** with top contributors

### Contributor Badges

- 🥇 **Founder**: First 10 contributors
- 🏆 **Top Contributor**: 20+ prompts accepted
- 🌟 **Quality Champion**: High approval rate
- 🌍 **Global Helper**: Translations contributor
- 🛡️ **Maintainer**: Helps review submissions

## 🚫 What We Don't Accept

### Content Restrictions

- ❌ Copied prompts without permission
- ❌ Generated spam or low-effort content
- ❌ Discriminatory or offensive material
- ❌ Prompts encouraging illegal activities
- ❌ Content that violates AI provider terms

### Technical Restrictions

- ❌ Invalid JSON format
- ❌ Missing required fields
- ❌ Overly complex or confusing prompts
- ❌ Prompts that don't work consistently
- ❌ Duplicate content without improvement

## 🆘 Getting Help

### Channels

- **GitHub Issues**: Technical problems
- **Discord**: `#contributors` channel
- **Email**: contribute@globalpromptlibrary.org

### Common Issues

**Q: My JSON won't validate**
A: Use online JSON validators and check for missing commas, quotes

**Q: Which category should I choose?**
A: Pick the primary use case. When unsure, ask in Discord

**Q: Can I update my pack later?**
A: Yes! Submit PRs for updates anytime

**Q: How do I handle variables in different languages?**
A: Keep variable names in English, but translate descriptions

## 📊 Metrics & Impact

Track your contribution impact:

- **Downloads**: How many times your pack is downloaded
- **Stars**: Community appreciation
- **Usage**: Apps integrating your prompts
- **Feedback**: Reviews and improvements

## 🎉 Onboarding Checklist

For new contributors:

- [ ] Read this guide completely
- [ ] Join Discord server
- [ ] Look at existing packs for inspiration
- [ ] Choose your first contribution type
- [ ] Set up development environment
- [ ] Create your first pack
- [ ] Submit pull request
- [ ] Respond to review feedback
- [ ] Celebrate your contribution! 🎉

## 🔮 Roadmap

Upcoming features for contributors:

- **Prompt Studio**: Visual prompt builder
- **Analytics Dashboard**: Track your impact
- **Bounty System**: Paid requests for specific prompts
- **API Access**: Programmatic contributions
- **Advanced Testing**: Automated quality checks

---

**Thank you for helping democratize AI prompts!** 

Every contribution makes AI more accessible to everyone. Let's build something amazing together! 🚀