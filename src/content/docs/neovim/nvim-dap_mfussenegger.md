
---
title: nvim-dap
---

### [mfussenegger nvim-dap](https://github.com/mfussenegger/nvim-dap)

### 核心内容总结

**项目功能**  
`nvim-dap` 是 Neovim 的 Debug Adapter Protocol（DAP）客户端实现，支持以下调试功能：  
- 启动或附加到调试目标  
- 设置断点（含条件、日志点、异常断点）  
- 逐步执行代码（步过、步入、步出、反向执行）  
- 检查变量状态（通过 REPL、UI 插件或虚拟文本）  

**使用方法**  
1. 安装方式：  
   - 手动克隆仓库  
   - 使用 `vim-plug` 或 `packer.nvim` 插件管理器  
2. 基本操作：  
   - 设置断点：`:DapToggleBreakpoint`  
   - 启动调试：`:DapNew` + `:DapContinue`  
   - 逐步执行：`:DapStepOver` / `:DapStepInto`  
   - 查看状态：通过 REPL（`:lua require'dap'.repl.open()`）或 UI 插件（如 `nvim-dap-ui`）  

**主要特性**  
- 支持所有有 DAP 适配器的语言（如 Python、JavaScript 等）  
- 提供 REPL、线内变量查看（`nvim-dap-virtual-text`）等调试辅助工具  
- 支持自定义快捷键（如方向键映射调试操作）  
- 可扩展性：允许通过插件（如 `nvim-dap-ui`）增强 UI 体验  

**注意事项**  
- 需自行安装并配置语言对应的 DAP 适配器  
- 不包含调试适配器的安装管理，建议通过系统包管理器或语言工具链处理  
- 提供中文文档（`:help dap.txt`）和社区维护的适配器配置指南