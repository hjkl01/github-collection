
---
title: nvim-lint
---

### [mfussenegger nvim-lint](https://github.com/mfussenegger/nvim-lint)  ![GitHub Repo stars](https://img.shields.io/github/stars/mfussenegger/nvim-lint?style=social)

nvim-lint 是一款适用于 Neovim (>= 0.9.5) 的异步 Linter 插件，作为内置语言服务器协议（LSP）的补充。它通过调用外部 Linter 工具、解析输出并通过 `vim.diagnostic` 模块报告诊断结果。项目内置支持数十种主流 Linter 工具，支持按文件类型配置，可通过自动命令（如 `BufWritePost`）触发检查。此外，允许用户注册自定义 Linter 及配置解析器（支持 Lua 模式、errorformat、SARIF），并提供诊断显示自定义、命名空间隔离及运行状态查询功能。