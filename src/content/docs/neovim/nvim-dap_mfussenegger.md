
---
title: nvim-dap
---

### [mfussenegger nvim-dap](https://github.com/mfussenegger/nvim-dap)  ![GitHub Repo stars](https://img.shields.io/github/stars/mfussenegger/nvim-dap?style=social)

`nvim-dap` 是 Neovim 的调试适配器协议（DAP）客户端插件。核心功能包括：启动或附加调试目标、设置与管理断点（支持条件、日志及异常断点）、控制代码执行流程（单步越过/进入/跳出、跳转、重启、暂停及反向继续）、检查运行时状态（变量、线程、堆栈及表达式求值）。它支持多种语言（需配置对应调试适配器），提供内置 REPL、UI 组件及扩展接口，旨在作为 Neovim 的基础调试工具及供其他插件调用的 DAP 库。