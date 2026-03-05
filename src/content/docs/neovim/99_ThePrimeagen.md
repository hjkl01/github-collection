
---
title: 99neovim
---

### [ThePrimeagen 99](https://github.com/ThePrimeagen/99)  ![GitHub Repo stars](https://img.shields.io/github/stars/ThePrimeagen/99?style=social)

99 是专为 Neovim 设计的 AI 客户端插件，旨在通过大语言模型增强而非替代程序员。主要功能包括：

1. **项目搜索**：根据提示词在项目范围内搜索内容，结果生成在快速修复列表中。
2. **视觉替换**：在 Visual 模式下选中代码，结合提示词使用 AI 结果直接替换选区内容。
3. **任务工作流**：通过 Worker 功能持久化跟踪任务描述及剩余待办事项。
4. **上下文增强**：提示词中支持使用 `#` 引用规则文件、`@` 引用项目文件，自动将内容注入 AI 上下文。
5. **多模型支持**：兼容 OpenCode、Claude、Cursor、Gemini 等 AI 后端，支持灵活配置与动态切换提供商及模型。
6. **扩展与配置**：集成 Telescope 和 fzf-lua 提供模型/提供商选择器；支持 Lua 配置日志、临时目录及文件排除；提供日志查看、停止请求等管理功能。
7. **状态**：当前处于 Beta 阶段，API 可能存在变更。
