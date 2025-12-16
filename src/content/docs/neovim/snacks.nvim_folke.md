
---
title: snacks.nvim
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/folke/snacks.nvim?style=social) ](https://github.com/folke/snacks.nvim)
### [folke snacks.nvim](https://github.com/folke/snacks.nvim)

**项目核心内容总结：**  

**功能**：  
Snacks 是一个 Neovim 插件，集成文件管理、终端控制、LSP 符号跳转、Zen 模式、通知管理、Git 操作等功能，支持快速切换缓冲区、删除文件、查看诊断信息、管理颜色主题等。  

**使用方法**：  
- 通过 `<leader>` 快捷键组合（如 `<leader>z` 进入 Zen 模式，`<leader>gB` 浏览 Git 仓库）调用功能。  
- 使用 `Snacks.picker` 系列命令（如 `grep`、`lsp_symbols`）进行搜索和导航。  
- 自定义快捷键映射（如 `<leader>us` 切换拼写检查）。  

**主要特性**：  
- 提供 100+ 预设快捷键，覆盖文件、终端、LSP、Git 等场景。  
- 支持 Zen 模式（全屏专注编辑）和通知系统（实时显示提示信息）。  
- 可通过 `init` 配置自定义调试工具（如 `dd` 查看变量值）。  
- 模块化设计，支持通过 `Snacks.toggle` 快速切换选项（如显示行号、语法高亮）。