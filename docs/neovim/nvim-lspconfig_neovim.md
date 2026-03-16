### [neovim nvim-lspconfig](https://github.com/neovim/nvim-lspconfig)  ![GitHub Repo stars](https://img.shields.io/github/stars/neovim/nvim-lspconfig?style=social)

nvim-lspconfig 是 Neovim 的 LSP 服务器配置集合，旨在为 Neovim LSP 客户端提供特定语言服务器的预置配置。

- **核心功能**：提供多种 LSP 服务器的配置文件（位于 `lsp/` 目录），支持通过 `vim.lsp.config` 自定义或扩展配置。
- **版本要求**：需 Neovim 0.11.3+，旧版 `require('lspconfig')` 配置框架已弃用，相关模块将被移除。
- **管理命令**：提供 `:LspInfo` 查看服务器状态，`:lsp enable/disable/restart` 控制服务器启用与停止。
- **启用方式**：安装对应语言服务器后，使用 `vim.lsp.enable` 启用配置，并满足项目根目录标记要求即可自动启用 LSP 功能。
- **支持说明**：配置由社区支持贡献，LSP 核心功能 Bug 请向 Neovim 核心仓库报告。