
---
title: nvim-lspconfig
---

### [neovim nvim-lspconfig](https://github.com/neovim/nvim-lspconfig)

### 核心内容总结

**项目功能**  
`nvim-lspconfig` 是为 Neovim LSP 客户端提供语言服务器（LSP）配置的工具集，支持多种语言服务器的配置与自定义，帮助用户在 Neovim 中实现代码补全、诊断、跳转等功能。

**使用方法**  
1. **安装**：可通过 Git 克隆到 Neovim 的 `pack` 目录，或使用 Neovim 0.12+ 的 `vim.pack` 插件管理器安装。  
2. **启用配置**：在 `init.lua` 中使用 `vim.lsp.enable('server_name')` 启用特定语言服务器，如 `vim.lsp.enable('pyright')`。  
3. **自定义配置**：通过 `vim.lsp.config('server_name', {设置项})` 修改服务器参数（如路径、设置等）。  
4. **健康检查**：运行 `:checkhealth vim.lsp` 检查配置是否生效及问题。

**主要特性**  
- **兼容性**：支持 Neovim 0.11+，旧版配置已弃用，推荐使用 `vim.lsp.config` 替代 `require('lspconfig')`。  
- **配置优先级**：自定义配置（如 `lsp/<server>.lua`）优先于默认配置，用户可覆盖默认行为。  
- **迁移指南**：提供从旧版 `require('lspconfig')` 迁移到新方式的说明。  
- **贡献支持**：支持用户提交新的语言服务器配置，需遵循 `CONTRIBUTING.md` 的格式要求。  
- **实用命令**：如 `:LspStart`、`:LspRestart`、`:LspStop` 可动态管理语言服务器的启动与停止。  

**注意事项**  
- 旧版 `require('lspconfig')` 方式已弃用，需迁移至新 API。  
- 配置文件优先级为：用户自定义配置 > 默认配置。  
- 健康检查命令 `:LspStart` 和 `:checkhealth` 可用于调试和验证配置。