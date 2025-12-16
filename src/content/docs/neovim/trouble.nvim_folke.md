
---
title: trouble.nvim
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/folke/trouble.nvim?style=social) ](https://github.com/folke/trouble.nvim)
### [folke trouble.nvim](https://github.com/folke/trouble.nvim)

**项目功能**  
Trouble 是一个 Neovim 插件，用于集中展示和管理搜索结果（如 Telescope、fzf-lua 的搜索结果）、代码问题（如 LSP 错误/警告）、文档符号（如 LSP 文档结构）等，支持通过窗口交互、跳转、折叠树形结构、预览等操作快速定位内容。

**使用方法**  
1. **集成搜索工具**：通过自定义快捷键（如 Telescope 的 `<c-t>`）将搜索结果导入 Trouble 窗口。  
2. **操作功能**：支持跳转到文件、预览内容、折叠/展开树形结构、关闭窗口等。  
3. **状态栏集成**：通过 Lualine 等插件在状态栏显示当前 Trouble 信息（如文档符号）。  

**主要特性**  
- **多源支持**：兼容 Telescope、fzf-lua、LSP 等工具的结果。  
- **交互操作**：提供跳转、预览、折叠节点、自动刷新等功能。  
- **高度自定义**：支持高亮颜色、窗口布局、快捷键映射、状态栏组件样式等自定义配置。  
- **API 扩展**：提供丰富的 Lua API，允许开发者扩展功能或集成到其他插件中。