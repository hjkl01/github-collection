
---
title: nvim-lsp-setup
---

### [Junnplus nvim-lsp-setup](https://github.com/Junnplus/nvim-lsp-setup)  ![GitHub Repo stars](https://img.shields.io/github/stars/Junnplus/nvim-lsp-setup?style=social)

lsp-setup.nvim 是一个基于 nvim-lspconfig 和 mason-lspconfig 的 Neovim LSP 配置包装器，旨在简化语言服务器的安装与设置。核心功能包括：
1. 通过简洁配置安装和配置 LSP 服务器，支持自定义版本。
2. 提供统一的 Inlay Hints 配置选项，适配多种语言服务器。
3. 内置常用 LSP 操作默认映射（如跳转定义、悬停、格式化等）并支持自定义覆盖。
4. 支持全局 on_attach 配置及与 cmp、lazydev、rust-tools 等插件的集成。