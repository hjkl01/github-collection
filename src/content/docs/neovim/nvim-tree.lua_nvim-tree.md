
---
title: nvim-tree.lua
---

### [nvim-tree nvim-tree.lua](https://github.com/nvim-tree/nvim-tree.lua)

### 项目概述

**项目名称**：为 Neovim 编写的 Lua 文件管理器（`nvim-tree`）  
**功能特性**：
- 自动更新文件内容
- 支持文件类型图标显示
- 集成 Git 功能
- 支持 LSP 和 COC 的诊断功能
- 实时过滤功能
- 提供剪切、复制、粘贴、重命名、删除、创建等操作
- 高度可定制化

---

### 系统要求

- **Neovim 版本**：需 ≥ 0.9.0  
- **可选插件**：`nvim-web-devicons`（用于显示文件图标）  
- **推荐配置**：禁用 Neovim 的默认文件管理器 `netrw`（通过设置 `vim.g.loaded_netrw = 1` 和 `vim.g.loaded_netrwPlugin = 1`）
