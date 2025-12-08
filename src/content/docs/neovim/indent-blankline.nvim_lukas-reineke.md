
---
title: indent-blankline.nvim
---

### [lukas-reineke indent-blankline.nvim](https://github.com/lukas-reineke/indent-blankline.nvim)

**项目功能**  
Indent Blankline 是一个 Neovim 插件，通过虚拟文本功能显示缩进引导线，帮助用户直观识别代码层级，无需使用隐藏（conceal）功能。

**使用方法**  
1. 安装：通过 Lazy.nvim 或 PCKR.nvim 等插件管理器安装。  
2. 配置：调用 `require("ibl").setup()` 初始化插件，可传入配置表自定义选项（如颜色、作用域高亮等）。

**主要特性**  
- 支持自定义缩进线颜色（如彩虹色系）。  
- 可显示代码作用域范围（需 Treesitter 支持）。  
- 兼容混合缩进场景（如不同语言混用）。  
- 支持背景色引导线及与 `rainbow-delimiters.nvim` 插件集成。  
- 高度可配置，支持动态调整高亮颜色以适配主题变化。  

**要求**  
需使用 Neovim 最新稳定版。