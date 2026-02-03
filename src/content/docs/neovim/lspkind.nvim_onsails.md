
---
title: lspkind.nvim
---

### [onsails lspkind.nvim](https://github.com/onsails/lspkind.nvim)  ![GitHub Repo stars](https://img.shields.io/github/stars/onsails/lspkind.nvim?style=social)

**项目功能**  
lspkind.nvim 为 Neovim 的补全菜单（LSP、代码片段、路径等）添加类似 VS Code 的图标，提升补全项的可读性和可扫描性，使类型和意图一目了然。

**使用方法**  
1. **原生 Neovim LSP**：在 LSP 配置中调用 `require('lspkind').init({})`，设置图标风格（如 `preset = 'codicons'`）和自定义符号映射。  
2. **nvim-cmp 插件**：通过 `lspkind.cmp_format` 集成到补全菜单，配置 `formatting` 字段。  
3. **blink.cmp 插件**：通过 `kind_icon` 组件调用 `require('lspkind').symbol_map` 获取图标。  

**主要特性**  
- 支持 LSP、代码片段、路径等补全类型；  
- 提供 `default`（Nerd Fonts）和 `codicons`（VS Code 图标）两种预设图标方案；  
- 可自定义每种补全类型和外部来源的图标；  
- 无依赖，轻量且 API 简单；  
- 适配 Neovim 0.7+，需安装对应字体（Nerd Fonts 或 VS Code Codicons）。