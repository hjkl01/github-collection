
---
title: smear-cursor.nvim
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/sphamba/smear-cursor.nvim?style=social) ](https://github.com/sphamba/smear-cursor.nvim)
### [sphamba smear-cursor.nvim](https://github.com/sphamba/smear-cursor.nvim)

**项目功能**  
为 Neovim 提供终端中的动画光标效果（类似 Neovide 的光标动画），适用于无法显示图形的终端环境，支持光标拖尾、插入模式动画等。

**使用方法**  
- 安装：通过 [lazy.nvim](https://lazy.folke.io/) 或 [vim-plug](https://github.com/junegunn/vim-plug) 添加插件。  
- 配置：启用插件后，使用 `:SmearCursorToggle` 或 Lua 脚本切换动画；通过 `opts` 调整参数（如动画速度、颜色、阻尼等）。

**主要特性**  
- 支持切换缓冲区/窗口时的光标拖尾效果。  
- 可配置动画参数（如 `stiffness`、`damping`、`time_interval`），调整动画流畅度和速度。  
- 适配透明背景和无图形字体（如 Cascadia Code），减少阴影干扰。  
- 提供插入模式下的光标动画，兼容 `termguicolors` 和无 GUI 颜色模式。  

**注意事项**  
- 部分终端可能因颜色覆盖导致光标阴影，需手动设置 `cursor_color` 或 `transparent_bg_fallback_color`。  
- 与修改光标的其他插件可能存在兼容性问题。