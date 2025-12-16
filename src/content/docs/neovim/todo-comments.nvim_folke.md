
---
title: todo-comments.nvim
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/folke/todo-comments.nvim?style=social) ](https://github.com/folke/todo-comments.nvim)
### [folke todo-comments.nvim](https://github.com/folke/todo-comments.nvim)

**项目核心内容总结：**

**功能**  
`todo-comments` 是 Neovim 0.8.0+ 的 Lua 插件，用于高亮和搜索代码中的待办事项注释（如 `TODO`、`HACK`、`BUG` 等），支持通过快捷键跳转、快速修复列表、Trouble 插件、Telescope 和 FzfLua 搜索。

**主要特性**  
- 多种样式高亮 TODO 注释  
- 通过 TreeSitter 限定在注释中高亮  
- 可自定义符号（signs）和颜色  
- 支持快速修复列表（Quickfix）和 Trouble 插件展示  
- 集成 Telescope/FzfLua 搜索 TODO 注释  

**使用方法**  
1. **快捷键跳转**：`]t`（下一个）、`[t`（上一个），可指定关键词过滤（如 `ERROR`、`WARNING`）。  
2. **命令**：  
   - `:TodoQuickFix`：显示所有 TODO 的快速修复列表  
   - `:TodoLocList`：显示位置列表  
   - `:Trouble todo`：通过 Trouble 插件查看 TODO  
   - `:TodoTelescope` / `:TodoFzfLua`：通过 Telescope/FzfLua 搜索 TODO  

**依赖**  
- Neovim 0.8.0+（旧版本需使用 `neovim-pre-0.8.0` 分支）  
- 建议安装 [ripgrep](https://github.com/BurntSushi/ripgrep) 和 [plenary.nvim](https://github.com/nvim-lua/plenary.nvim)  
- 可选集成：[Trouble](https://github.com/folke/trouble.nvim)、[Telescope](https://github.com/nvim-telescope/telescope.nvim)、[FzfLua](https://github.com/ibhagwan/fzf-lua)  

**安装**  
使用 Lazy.nvim 安装，需依赖 `plenary.nvim`，配置支持自定义关键词、颜色、高亮样式等。