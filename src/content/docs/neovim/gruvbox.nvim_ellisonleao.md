
---
title: gruvbox.nvim
---

### [ellisonleao gruvbox.nvim](https://github.com/ellisonleao/gruvbox.nvim)  ![GitHub Repo stars](https://img.shields.io/github/stars/ellisonleao/gruvbox.nvim?style=social)

**项目核心内容总结**  

**功能**：  
将 [gruvbox community](https://github.com/gruvbox-community/gruvbox) 主题移植为 Lua 实现，支持 [treesitter](https://github.com/nvim-treesitter/nvim-treesitter) 和 LSP 语义高亮，提供丰富的颜色主题配置。  

**使用方法**：  
1. 安装方式：支持 `packer`、`lazy.nvim` 或 `vim-plug` 安装。  
2. 配置：在 `init.vim` 或 `init.lua` 中设置背景（`dark`/`light`）并调用 `colorscheme gruvbox`。  

**主要特性**：  
- 支持终端颜色、下划线、粗体、斜体、删除线等样式。  
- 可自定义调色板（`palette_overrides`）和高亮组（`overrides`），覆盖特定语法或语义高亮颜色。  
- 提供多种配置选项，如 `contrast`（对比度）、`transparent_mode`（透明模式）、`inverse`（反色高亮）等。  
- 需在调用 `colorscheme` 前通过 `require("gruvbox").setup()` 初始化配置。