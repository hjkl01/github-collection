
---
title: rustaceanvim
---

### [mrcjkb rustaceanvim](https://github.com/mrcjkb/rustaceanvim)  ![GitHub Repo stars](https://img.shields.io/github/stars/mrcjkb/rustaceanvim?style=social)

rustaceanvim 是一个专为 Neovim 打造的 Rust 开发增强插件，基于 rust-analyzer LSP 客户端。它无需 setup 函数即可自动工作，不依赖 nvim-lspconfig。主要功能包括：调试集成（支持 nvim-dap 和 codelldb）、运行与测试管理、Neotest 适配，以及丰富的 Rust 特定 LSP 命令（如宏展开、代码重构、错误解释、诊断渲染、依赖图谱及 HIR/MIR 查看）。支持通过 `vim.g.rustaceanvim` 灵活配置，适用于 Neovim 0.11+ 环境。