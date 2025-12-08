
---
title: codecompanion.nvim
---

### [olimorris codecompanion.nvim](https://github.com/olimorris/codecompanion.nvim)

**项目简介**  
CodeCompanion.nvim 是一个基于 Neovim 的插件，通过集成 LLM（如 Anthropic、OpenAI、Gemini 等）和代理（如 Augment Code、Cagent 等）提供代码辅助功能，支持自定义适配器、内联编辑、多聊天窗口、图像输入等特性。

**核心功能**  
1. **LLM/代理支持**：兼容 Anthropic、Copilot、OpenAI、Gemini、Mistral 等主流模型，及 Agent Client Protocol（ACP）协议的代理（如 Docker Cagent、Claude Code 等）。  
2. **交互功能**：提供内联代码转换、多聊天窗口、变量/工具/工作流管理、记忆文件（如 `CLAUDE.md`）支持。  
3. **扩展性**：支持自定义适配器、提示语、变量和命令，社区贡献适配器可直接使用。  
4. **辅助工具**：内置 Super Diff 跟踪修改、提示库（如 LSP 错误建议）、异步执行提升性能。  

**使用方法**  
- 安装依赖后通过 `:checkhealth codecompanion` 检查配置，参考 [官方文档](https://codecompanion.olimorris.dev) 配置和使用。  
- 故障排查：开启调试日志（`log_level = "DEBUG"`），或使用 `minimal.lua` 测试配置。  

**主要特性**  
- 支持图像输入、多模型/代理协作、自定义工具链。  
- 提供视频演示（如内联助手、工具工作流等）。  
- 依赖 `nvim-treesitter` 和 `plenary.nvim` 等基础库。