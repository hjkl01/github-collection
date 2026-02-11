
---
title: 99 neovim
---

### [ThePrimeagen 99](https://github.com/ThePrimeagen/99)  ![GitHub Repo stars](https://img.shields.io/github/stars/ThePrimeagen/99?style=social)

**项目简介：99 - Neovim 的 AI 客户端**

**核心功能：**  
99 是一个为 Neovim 设计的 AI 客户端，旨在通过限制请求范围，为开发者提供更高效的 AI 协作体验。它支持通过 `#` 引用自定义规则（SKILL.md），通过 `@` 快速搜索并引用项目文件，从而增强 AI 请求的上下文。目前支持的 AI 提供商包括 opencode、claude 和 cursor-agent。

**主要特性：**  
- **AI 集成：** 支持多种 AI CLI 工具，提供自动补全和上下文增强。
- **自定义规则：** 可配置自定义规则目录，自动识别并加载规则文件（SKILL.md）。
- **文件引用：** 支持通过 `@` 模糊搜索项目文件，自动注入内容到 AI 请求中。
- **可视化选择：** 支持在可视模式下选择代码块发送给 AI。
- **日志支持：** 提供调试日志记录，便于跟踪请求过程。
- **语言支持：** 当前支持 TypeScript 和 Lua，未来计划扩展更多语言。
- **API 功能：** 提供 visual、search（开发中）和 debug（计划中）等 API。

**使用方法：**  
1. 安装支持的 AI CLI 工具（如 opencode、claude 或 cursor-agent）。
2. 在 Neovim 配置中加载 99 插件（推荐使用 Lazy 插件管理器）。
3. 配置 99，设置日志路径、自定义规则目录、文件引用规则等。
4. 使用快捷键（如 `<leader>9v`）发送可视选择内容给 AI，或使用 `#`/`@` 引用规则/文件。

**注意事项：**  
- 项目仍处于 alpha 阶段，API 可能频繁变动。
- 部分功能（如 search）尚未完成，可能存在使用限制。
- 项目不建议用于一般性 AI 请求，建议使用 opencode。
