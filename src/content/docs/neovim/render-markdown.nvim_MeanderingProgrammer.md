
---
title: render-markdown.nvim
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/MeanderingProgrammer/render-markdown.nvim?style=social) ](https://github.com/MeanderingProgrammer/render-markdown.nvim)
### [MeanderingProgrammer render-markdown.nvim](https://github.com/MeanderingProgrammer/render-markdown.nvim)

**项目核心内容总结：**  
`render-markdown.nvim` 是一个 Vim 插件，用于美化 Markdown 文档的显示，提供语法高亮、代码块、表格、列表、数学公式等元素的渲染支持。  

**主要功能：**  
- **语法高亮与渲染**：支持标题、代码块、表格、列表、数学公式等 Markdown 元素的语法高亮和视觉美化。  
- **集成 Treesitter**：基于语法树解析 Markdown，提升渲染准确性。  
- **自定义配置**：用户可通过 Lua 脚本自定义高亮颜色、缩进样式、链接图标等。  
- **兼容性支持**：与 `vimwiki` 和 `obsidian.nvim` 插件兼容，需在配置中禁用 `obsidian.nvim` 的默认 UI。  
- **代码块增强**：支持代码块语言检测与语法高亮，兼容常见编程语言。  

**使用方法：**  
1. 安装插件后，通过 Lua 配置启用功能（如 `file_types = { 'markdown', 'vimwiki' }`）。  
2. 注册 `markdown` 为 `vimwiki` 文件的解析器（需调用 `vim.treesitter.language.register`）。  
3. 可选配置缩进、符号、链接样式等参数。  

**注意事项：**  
- 与 `obsidian.nvim` 共存时需禁用其 UI 功能。  
- 图像渲染仅提供基础支持，建议启用 `only_render_image_at_cursor` 避免冲突。  
- 部分功能可能存在限制，可通过自定义处理程序扩展。