
---
title: mason-lspconfig.nvim
---

### [mason-org mason-lspconfig.nvim](https://github.com/mason-org/mason-lspconfig.nvim)

### 核心内容总结

**项目功能**  
`mason-lspconfig.nvim` 是一个 Neovim 插件，用于连接 `mason.nvim`（包管理器）与 `nvim-lspconfig`（LSP 配置插件），实现以下功能：  
- 自动安装并启用通过 `mason.nvim` 安装的 LSP 服务器（如 `lua_ls`、`rust_analyzer` 等）。  
- 提供便捷命令（如 `:LspInstall`、`:LspUninstall`）管理 LSP 服务器。  
- 翻译 `nvim-lspconfig` 服务器名称与 `mason.nvim` 包名的对应关系。  

**使用方法**  
1. 安装插件（需 `neovim >= 0.11.0`、`mason.nvim >= 2.0.0`、`nvim-lspconfig >= 2.0.0`）。  
2. 调用 `require("mason-lspconfig").setup()` 初始化。  
3. 推荐 `lazy.nvim` 用户使用以下配置：  
   ```lua
   {
     "mason-org/mason-lspconfig.nvim",
     opts = { ensure_installed = { "lua_ls", "rust_analyzer" } },
     dependencies = { "mason-org/mason.nvim", "neovim/nvim-lspconfig" },
   }
   ```  

**主要特性**  
- **自动启用**：默认自动启用已安装的 LSP 服务器，可通过配置 `automatic_enable` 关闭或限制范围（如排除某些服务器）。  
- **灵活配置**：支持 `ensure_installed` 指定需自动安装的服务器列表。  
- **命令支持**：提供 `:LspInstall`（安装服务器）和 `:LspUninstall`（卸载服务器）命令。