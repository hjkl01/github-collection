
---
title: tokyonight.nvim
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/folke/tokyonight.nvim?style=social) ](https://github.com/folke/tokyonight.nvim)
### [folke tokyonight.nvim](https://github.com/folke/tokyonight.nvim)

**项目功能**：TokyoNight 是一个为 Neovim 设计的色彩主题插件，提供四种风格（storm、moon、night、day），支持透明模式、自定义颜色和高亮组，兼容多个插件（如 Lualine、Barbecue）。  

**使用方法**：通过 Lua 脚本调用 `require("tokyonight").setup()` 配置主题，设置 `style` 参数选择风格，使用 `on_colors` 和 `on_highlights` 自定义颜色与高亮；需在加载主题前完成配置。  

**主要特性**：  
1. **多风格支持**：提供 storm（深色）、moon（较亮）、night（更暗）、day（浅色）四种主题；  
2. **高度自定义**：可调整颜色、亮度、透明度，支持插件兼容性配置；  
3. **插件适配**：自动适配 Lualine、Barbecue 等插件，部分插件需额外配置；  
4. **性能优化**：支持缓存功能提升加载速度，适配终端（如 Kitty、Alacritty）和 Tmux 环境。