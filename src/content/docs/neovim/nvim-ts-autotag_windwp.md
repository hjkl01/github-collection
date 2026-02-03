
---
title: nvim-ts-autotag
---

### [windwp nvim-ts-autotag](https://github.com/windwp/nvim-ts-autotag)  ![GitHub Repo stars](https://img.shields.io/github/stars/windwp/nvim-ts-autotag?style=social)

**项目功能**  
`nvim-ts-autotag` 是一个基于 Neovim 的插件，利用 Treesitter 实现 HTML 标签的**自动闭合**和**自动重命名**，支持多种文件类型（如 HTML、JSX、Vue、XML 等）。  

**使用方法**  
- 输入 `>` 自动闭合标签（如 `<div` → `<div></div>`）。  
- 使用 `ciwspan<esc>` 替换标签（如 `<div></div>` → `<span></span>`）。  
- 通过 Lua 配置启用功能（如 `enable_close`、`enable_rename`）。  

**主要特性**  
1. **多语言支持**：兼容 HTML、JSX、Vue、XML、Markdown 等 20+ 文件类型。  
2. **灵活配置**：可全局或按文件类型（如 `html`）单独设置功能开关。  
3. **扩展性**：支持为新语言设置别名（如将 `your language` 映射到 `html` 配置），或直接覆盖默认配置（如修改标签匹配规则）。  
4. **兼容性**：需 Neovim 0.9.5+ 及 Treesitter 解析器，支持延迟加载。  

**注意事项**  
- 旧版 `nvim-treesitter.configs` 配置方式已弃用，需迁移至新方法。  
- 若需延迟加载，建议使用 `BufReadPre` 或 `BufNewFile` 事件。  
- 需通过 LSP 设置 `update_in_insert = true` 解决插入时更新问题。