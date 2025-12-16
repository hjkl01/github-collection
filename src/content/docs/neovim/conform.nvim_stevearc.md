
---
title: conform.nvim
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/stevearc/conform.nvim?style=social) ](https://github.com/stevearc/conform.nvim)
### [stevearc conform.nvim](https://github.com/stevearc/conform.nvim)

**项目功能**  
conform.nvim 是一个 Neovim 插件，用于代码格式化，支持自定义 formatter（如 Prettier、Black 等）和 LSP 集成，可灵活控制格式化行为。

**使用方法**  
1. 通过 Lua 配置 formatter，定义格式化规则（如设置 `formatters` 表、`lsp_format` 参数等）。  
2. 调用 `conform.format()` 函数触发格式化，支持同步/异步模式、范围选择（Visual Mode）和 LSP 优先级控制。  

**主要特性**  
- 支持异步格式化，避免 UI 卡顿。  
- 可定义 formatter 的执行顺序、超时时间、是否合并 undo 操作等。  
- 提供范围格式化功能（通过 Visual Mode 选择区域）。  
- LSP 格式化可设为“永不使用”“备用”“优先”等模式，兼容其他 formatter。  
- 支持错误通知、日志记录及 formatter 可用性检查。