
---
title: lingo.dev
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/lingodotdev/lingo.dev?style=social) ](https://github.com/lingodotdev/lingo.dev)
### [lingodotdev lingo.dev](https://github.com/lingodotdev/lingo.dev)

Lingo.dev 是一个开源的 AI 驱动国际化工具包，通过大型语言模型实现即时本地化。项目包含多个工具：

1. **编译器**：在构建时自动将 React 应用本地化，无需修改现有组件。通过 `npm install lingo.dev` 安装，配置 Next.js 项目后运行 `next build` 即可生成多语言包。

2. **CLI**：终端命令行工具，支持代码和内容的一键翻译，仅重新翻译变更内容。

3. **CI/CD**：自动化翻译流程，通过 GitHub Actions 配置，推送代码时自动提交翻译结果或创建 PR。

4. **SDK**：实时翻译用户生成内容，支持动态内容的即时本地化。

主要特性包括：无需改动现有代码、多语言支持、自动化翻译流程、实时翻译能力。