
---
title: nvim-lspconfig
---

### [neovim nvim-lspconfig](https://github.com/neovim/nvim-lspconfig)  ![GitHub Repo stars](https://img.shields.io/github/stars/neovim/nvim-lspconfig?style=social)

nvim-lspconfig 是一个为 Neovim LSP 客户端提供 LSP 服务器配置的集合插件。它包含针对多种编程语言的服务器设置文件，但本身不负责实现 LSP 协议。项目已弃用旧版 `require('lspconfig')` 框架，全面支持 Nvim 0.11.3+，推荐使用 `vim.lsp.enable` 启用服务器配置，并通过 `vim.lsp.config` 或 `after/lsp/` 目录进行自定义和扩展。主要功能包括：自动加载服务器配置、管理语言服务器状态、提供调试诊断工具（如 `:LspInfo`），以及支持社区贡献新的服务器配置。