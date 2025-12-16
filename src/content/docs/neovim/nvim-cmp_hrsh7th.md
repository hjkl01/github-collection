
---
title: nvim-cmp
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/hrsh7th/nvim-cmp?style=social) ](https://github.com/hrsh7th/nvim-cmp)
### [hrsh7th nvim-cmp](https://github.com/hrsh7th/nvim-cmp)

**项目功能**  
nvim-cmp 是一个基于 Neovim 的 Lua 编写的补全引擎插件，支持 LSP、缓冲区、路径、命令行等多类补全源，可自定义补全行为和键映射，提供无闪烁的补全体验。

**使用方法**  
1. 安装插件（如 `vim-plug` 管理），需搭配 LSP 服务器和补全源（如 `cmp-nvim-lsp`、`cmp-buffer` 等）。  
2. 配置 `lua` 脚本，设置补全源、映射（如 `<C-Space>` 触发补全）、窗口样式等。  
3. 根据需要选择片段插件（如 `vsnip`、`luasnip` 等），并配置对应的 `expand` 函数。  

**主要特性**  
- 完全支持 LSP 补全功能  
- 支持多种补全源（LSP、缓冲区、路径、命令行等）  
- 高度可定制，可通过 Lua 函数自定义行为  
- 智能处理键映射，避免冲突  
- 无闪烁补全界面  
- 提供预设的插入模式和命令行模式映射（`preset.insert`、`preset.cmdline`）  

**补充说明**  
- 需自行管理补全源和片段插件的安装  
- 配置需根据所选片段插件调整 `expand` 函数  
- 项目维护者建议自行处理键映射，不保证预设配置长期兼容性