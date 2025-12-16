
---
title: nvim-lsp-setup
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/Junnplus/nvim-lsp-setup?style=social) ](https://github.com/Junnplus/nvim-lsp-setup)
### [Junnplus nvim-lsp-setup](https://github.com/Junnplus/nvim-lsp-setup)

lsp-setup.nvim 是一个用于简化 Neovim 中 LSP 服务器配置的工具，支持与 `nvim-lspconfig` 和 `mason-lspconfig` 集成。其主要功能和特点包括：

1. **支持多种 LSP 服务器**  
   可安装和配置多种 LSP 服务器，如 `pylsp`、`clangd`、`rust-analyzer`、`gopls`、`lua_ls` 等，满足不同编程语言的开发需求。

2. **自定义版本安装**  
   通过 `mason-lspconfig` 支持安装自定义版本的 LSP 服务器，例如 `rust_analyzer@nightly`，提升灵活性。

3. **详细配置选项**  
   提供 Lua 脚本配置选项，例如：
   - **Inlay Hints**：通过 `inlay_hints` 设置参数名、函数返回类型等提示信息。
   - **诊断设置**：如 `lua_ls` 中配置 `globals = { 'vim' }`，避免 Neovim 全局变量的错误提示。
   - **Rust 工具链集成**：通过 `rust-analyzer` 的 `cargo` 和 `procMacro` 配置，增强 Rust 项目开发体验。

4. **插件集成**  
   与多个 Neovim 插件无缝集成，例如：
   - **cmp-nvim-lsp**：提升代码补全功能。
   - **lazydev**：简化插件管理与开发调试。
   - **rust-tools.nvim**：增强 Rust 语言支持，如代码导航、调试等。

5. **用户贡献机制**  
   支持用户通过提交 PR 或报告问题参与项目改进，推动工具持续优化。

**总结**  
lsp-setup.nvim 是一个功能强大且灵活的工具，旨在简化 Neovim 中 LSP 服务器的配置与集成，提升开发效率，适用于多种编程语言和开发场景。