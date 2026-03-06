
---
title: nvim-lsp-setup
---

### [Junnplus nvim-lsp-setup](https://github.com/Junnplus/nvim-lsp-setup)  ![GitHub Repo stars](https://img.shields.io/github/stars/Junnplus/nvim-lsp-setup?style=social)

lsp-setup.nvim 是基于 nvim-lspconfig 和 mason-lspconfig 的 Neovim LSP 配置封装工具。主要功能如下：

1. **简化 LSP 管理**：轻松配置和自动安装多种 LSP 服务器，支持指定自定义版本。
2. **内联提示支持**：支持全局开启或针对特定服务器（如 typescript, rust, gopls 等）精细配置 Inlay Hints。
3. **默认快捷键**：内置定义跳转、悬停、重命名等 LSP 操作映射，支持自定义覆盖及全局 `on_attach` 回调配置。
4. **插件集成**：自动适配 cmp-nvim-lsp、lazydev.nvim 和 rust-tools.nvim 等主流插件。