
---
title: none-ls.nvim
---

### [nvimtools none-ls.nvim](https://github.com/nvimtools/none-ls.nvim)

**项目核心内容总结：**

**功能**  
`none-ls.nvim`（原 `null-ls.nvim`）是一个 Neovim 插件，通过 Lua 实现 LSP 功能（如代码格式化、诊断、代码操作等），无需依赖外部语言服务器，提升性能并减少配置复杂度。

**使用方法**  
1. 安装：通过包管理器安装，需依赖 `plenary.nvim`。  
2. 配置：通过 Lua 注册内置或自定义源，例如：  
   ```lua  
   null_ls.setup({ sources = { null_ls.builtins.formatting.stylua } })  
   ```  
3. 支持通过 CLI 工具生成诊断（如 `markdownlint`）或自定义 Lua 逻辑（如检测 `really` 关键字）。

**主要特性**  
- 支持 LSP 的核心功能：格式化、诊断、代码操作、悬停提示、补全。  
- 内置多种语言工具源（如 `stylua`、`eslint`），可直接调用。  
- 提供 CLI 工具解析辅助函数，简化外部命令集成。  
- 纯 Lua 实现，无需外部进程，性能更优。  
- 社区协作维护，支持贡献者提交代码并审核。

**注意事项**  
- 项目处于 Beta 阶段，需兼容 Neovim 最新稳定版。  
- 调试时启用 `debug = true`，通过 `:NullLsLog` 查看日志。  
- 格式化超时可调整 `timeout_ms` 参数。  
- 避免与 LSP 插件冲突时，需配置 `formatting` 优先级。