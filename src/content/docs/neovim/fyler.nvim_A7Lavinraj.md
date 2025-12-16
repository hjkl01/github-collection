
---
title: fyler.nvim
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/A7Lavinraj/fyler.nvim?style=social) ](https://github.com/A7Lavinraj/fyler.nvim)
### [A7Lavinraj fyler.nvim](https://github.com/A7Lavinraj/fyler.nvim)

**Fyler.nvim 核心内容总结**  

**项目功能**  
Fyler.nvim 是 Neovim 的文件管理器插件，支持快速浏览、操作文件，提供多种窗口布局方式（如左侧分割窗口）。  

**使用方法**  
1. **命令方式**：通过 `:Fyler` 打开文件管理器，可指定目录路径或窗口类型（如 `:Fyler kind=split_left_most`）。  
2. **Lua API**：调用 `require('fyler').open()` 打开，默认使用当前目录；支持参数自定义目录或窗口布局（如 `fyler.open({ dir = "~", kind = "split_left_most" })`）。  
3. **快捷键映射**：可将 `:Fyler` 或 Lua API 绑定到自定义快捷键（如 `<leader>e`）。  

**主要特性**  
- 依赖 `mini.icons` 插件，支持文件图标显示。  
- 提供稳定分支（`stable`）确保生产环境兼容性。  
- 受多个 Neovim 插件（如 Telescope、Oil 等）启发，融合文件管理与窗口操作功能。  

**安装方法**  
推荐使用 [Lazy.nvim](https://github.com/folke/lazy.nvim) 安装，需添加依赖 `nvim-mini/mini.icons`，并指定 `branch = "stable"`。也可通过 [Mini.deps](https://github.com/echasnovski/mini.nvim) 安装。