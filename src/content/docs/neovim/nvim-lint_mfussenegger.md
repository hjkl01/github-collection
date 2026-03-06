
---
title: nvim-lint
---

### [mfussenegger nvim-lint](https://github.com/mfussenegger/nvim-lint)  ![GitHub Repo stars](https://img.shields.io/github/stars/mfussenegger/nvim-lint?style=social)

nvim-lint 是一款适用于 Neovim (>= 0.9.5) 的异步代码检查插件，用于补充内置 LSP 支持并运行独立 linter 工具。

核心功能：
1. 异步执行 linter 命令，解析输出并通过 `vim.diagnostic` 报告诊断信息。
2. 支持按文件类型配置 linter，通过自动命令（如保存后）触发检查。
3. 内置数十种常用 linter，支持自定义命令、参数及输出解析（Lua 模式、errorformat、SARIF）。
4. 允许修改内置 linter 属性，后处理诊断结果，或自定义诊断显示配置。
5. 支持查询当前运行中的 linter 列表。

注意：涉及执行外部命令，请勿在未信任的仓库中调用。