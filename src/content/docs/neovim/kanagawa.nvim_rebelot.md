
---
title: kanagawa.nvim
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/rebelot/kanagawa.nvim?style=social) ](https://github.com/rebelot/kanagawa.nvim)
### [rebelot kanagawa.nvim](https://github.com/rebelot/kanagawa.nvim)

**项目核心内容总结：**

**功能**  
Kanata 是一个受 Tokyonight、Gruvbox 等启发的 Neovim 主题，提供高可读性与视觉舒适的代码编辑体验，支持多语言语法高亮。

**使用方法**  
1. 安装 Neovim（需 v0.7+）；  
2. 通过 Lua 配置加载主题（如 `require("kanata").setup()`）；  
3. 安装依赖插件（如 lualine、nvim-tree）以适配主题样式。

**主要特性**  
- **多主题变体**：提供 wave、dragon、lotus 等预设风格；  
- **高度定制**：支持通过 Lua 脚本调整配色、背景等参数；  
- **可访问性**：符合 WCAG 2.1 AA 对比度标准（4.5:1）；  
- **兼容性**：适配 Alacritty、Kitty、iTerm2 等终端，含额外配置模板（如 Fish Shell、Emacs、Windows Terminal）；  
- **扩展性**：提供 Python 脚本提取图片色板，便于自定义主题。