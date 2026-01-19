
---
title: sidekick.nvim
---

### [folke sidekick.nvim](https://github.com/folke/sidekick.nvim)  ![GitHub Repo stars](https://img.shields.io/github/stars/folke/sidekick.nvim?style=social)

**项目功能**  
sidekick.nvim 是一款 Neovim 插件，提供两大核心功能：  
1. **Next Edit Suggestions (NES)**：基于 Copilot 的多行重构建议，支持暂停后生成跨文件的上下文编辑建议。  
2. **AI CLI 集成**：内置终端支持 Claude、Gemini、Copilot 等 CLI 工具，可直接在 Neovim 中调用 AI 功能。  

**使用方法**  
- **NES 功能**：通过 `:Sidekick nes enable/disable/toggle` 控制建议，或手动触发 `:Sidekick nes update`。  
- **CLI 工具**：使用 `:Sidekick cli show name=工具名` 打开指定 AI 工具，或通过 `:Sidekick cli send` 发送消息。  
- **自定义配置**：可添加自定义 AI 工具、提示语（如 `refactor`、`security` 等）及键位绑定。  

**主要特性**  
- 支持 Copilot 签名、LSP 附件检测及状态栏显示（兼容 lualine 等插件）。  
- 兼容多种 AI 工具（需提前安装 CLI，如 Claude、Gemini 等）。  
- 提供命令行接口（`:Sidekick`）直接调用 Lua API。  
- 支持 tmux/zellij 等终端复用工具，确保 CLI 会话持久化。  
- 无需 GitHub Copilot 订阅即可使用 CLI 功能，仅 NES 需 Copilot。