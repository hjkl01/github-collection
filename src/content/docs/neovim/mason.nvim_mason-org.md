
---
title: mason.nvim
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/mason-org/mason.nvim?style=social) ](https://github.com/mason-org/mason.nvim)
### [mason-org mason.nvim](https://github.com/mason-org/mason.nvim)

**项目功能**  
mason.nvim 是一个用于 Neovim 的包管理器，支持安装和管理语言服务器（LSP）、调试器（DAP）、代码检查工具（linters）和格式化工具（formatters）。它跨平台兼容（Linux、macOS、Windows），并自动将安装的工具路径添加到系统 PATH 中，实现无缝集成。

**使用方法**  
1. 通过 Neovim 插件管理器安装 mason.nvim。  
2. 调用 `require("mason").setup()` 初始化配置（或使用 lazy.nvim 的预设配置）。  
3. 使用命令如 `:Mason` 管理工具安装、更新、卸载（如 `:MasonInstall`、`:MasonUpdate`、`:MasonUninstall`）。  

**主要特性**  
- **跨平台支持**：适配所有主流操作系统。  
- **自动路径管理**：安装的工具自动添加到 PATH，无需手动配置。  
- **灵活配置**：支持自定义安装目录、并发安装限制、日志级别、UI 界面样式（如图标、窗口大小、快捷键）。  
- **依赖管理**：支持通过 GitHub、PyPI 等源获取包，可扩展注册表和元数据解析器。  
- **交互式界面**：提供可视化窗口管理工具，支持快捷键操作（如安装、更新、过滤语言等）。