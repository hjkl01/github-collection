
---
title: neotest
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/nvim-neotest/neotest?style=social) ](https://github.com/nvim-neotest/neotest)
### [nvim-neotest neotest](https://github.com/nvim-neotest/neotest)

**项目功能**  
Neotest 是一个用于 Neovim 的测试工具，支持运行、调试、收集测试结果，并提供可视化界面展示测试状态和输出。  

**使用方法**  
- 运行单个测试：`require("neotest").run.run()`  
- 运行当前文件：`require("neotest").run.run(vim.fn.expand("%"))`  
- 调试测试：`require("neotest").run.run({strategy = "dap"})`  
- 停止测试：`require("neotest").run.stop()`  
- 查看测试输出：通过 `:h neotest.output` 或 `:h neotest.output_panel` 查看结果。  

**主要特性**  
1. **多策略支持**：支持 `integrated`（后台运行）和 `dap`（调试）两种测试运行方式。  
2. **可视化工具**：提供输出窗口、摘要窗口、诊断信息、状态标志等，实时展示测试结果和状态。  
3. **自动监听**：通过 `:h neotest.watch` 监听文件变化并自动重跑相关测试。  
4. **适配器扩展**：支持自定义适配器，需实现测试解析、命令构造和结果收集三大功能，适用于不同测试框架（如 Plenary、Vim-test 等）。  
5. **跨语言支持**：基于 Treesitter 或正则表达式解析测试文件，兼容多种编程语言。  

**核心内容总结**  
Neotest 是 Neovim 的测试管理工具，提供测试运行、调试、结果收集及可视化展示功能，支持自定义适配器和多语言测试框架，提升开发效率。