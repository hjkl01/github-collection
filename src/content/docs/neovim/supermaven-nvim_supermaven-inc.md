
---
title: supermaven-nvim
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/supermaven-inc/supermaven-nvim?style=social) ](https://github.com/supermaven-inc/supermaven-nvim)
### [supermaven-inc supermaven-nvim](https://github.com/supermaven-inc/supermaven-nvim)

**项目功能**  
supermaven-nvim 是一个 Neovim 插件，用于在 Neovim 中集成 [Supermaven](https://supermaven.com/)，提供代码补全和智能提示功能。支持免费版和 Pro 版切换，可通过命令行或 Lua API 控制插件状态。

**使用方法**  
1. **安装**  
   使用 `lazy.nvim` 或 `packer.nvim` 安装插件，并通过 `require("supermaven-nvim").setup({})` 初始化配置。  
2. **配置**  
   可自定义按键映射（如 `<Tab>` 接受建议、`<C-]>` 清除建议）、忽略的文件类型（如 `cpp`）、建议文本颜色、日志级别等。  
3. **与 nvim-cmp 集成**  
   在 `cmp.setup` 中添加 `supermaven` 作为补全源，并可自定义图标和高亮样式。  

**主要特性**  
- 支持通过 `:SupermavenStart` 等命令控制插件启停、切换版本、查看日志。  
- 提供 Lua API（如 `api.start()`、`api.toggle()`）实现程序化控制。  
- 支持条件性禁用插件（如通过 `condition` 函数限制特定文件类型或场景）。  
- 可与 `nvim-cmp` 协同工作，兼容主流补全框架。