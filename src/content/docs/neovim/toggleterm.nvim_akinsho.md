
---
title: toggleterm.nvim
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/akinsho/toggleterm.nvim?style=social) ](https://github.com/akinsho/toggleterm.nvim)
### [akinsho toggleterm.nvim](https://github.com/akinsho/toggleterm.nvim)

**项目核心内容总结：**

toggleterm.nvim 是一个用于 Neovim 的终端管理插件，支持创建、切换和管理多个终端窗口，提供灵活的布局方式（垂直、水平、浮动窗口）和自定义配置。主要功能包括：

1. **终端管理**  
   - 支持通过快捷键（如 `:ToggleTerm`）快速打开/关闭终端，可自定义终端大小、布局方向、目录路径等。
   - 支持多终端并排显示（垂直/水平方向），但不支持标签页（tab）和浮动窗口（float）的并排。

2. **高级特性**  
   - **自定义终端**：可创建独立终端实例（如集成 `lazygit`、`htop` 等工具），设置专属命令、布局、快捷键及回调函数（如打开/关闭时的触发动作）。
   - **持久化配置**：保存终端窗口大小和位置，关闭后重新打开时保持一致。
   - **自动阴影调整**：默认为终端窗口添加暗色背景，可通过配置关闭或指定特定文件类型生效。
   - **快捷键映射**：支持在终端内自定义按键（如 `<Esc>` 返回编辑模式，`<C-h/j/k/l>` 切换窗口）。

3. **使用方法**  
   - 安装后通过 Lua 脚本配置（如设置 `shade_terminals`、`persist_size` 等参数）。
   - 使用 `Terminal:new()` 创建自定义终端，绑定快捷键调用。
   - 支持通过 `:TermGitPush` 等自定义命令快速执行终端操作。

4. **兼容性**  
   - 与 PowerShell 等外部工具兼容，需参考 Wiki 中的配置说明。