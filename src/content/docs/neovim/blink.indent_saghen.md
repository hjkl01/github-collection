
---
title: blink.indent
---

### [saghen blink.indent](https://github.com/saghen/blink.indent)

**项目核心内容总结**  
blink.indent 是一个高性能的缩进线插件，可在每次按键时实时显示缩进引导线（延迟约 0.1-1ms），支持超大文件。其缩进线适用于绝大多数合法代码，计算速度比 Treesitter 快约 10 倍。若需更丰富的功能，可考虑使用 indent-blankline 或 snacks.indent。

**使用方法**  
1. 安装：支持 Lazy.nvim 和 vim.pack 方式。  
2. 配置：通过 `setup()` 自定义选项，如禁用特定文件类型（如终端、帮助文档等）、设置缩进字符（默认 `▎`）、高亮颜色（支持多色渐变）及快捷键（如 `[i`/`]i` 跳转缩进层级）。  
3. 禁用：全局或单文件通过 `vim.g.indent_guide = false` 或 `vim.b[bufnr].indent_guide = false` 控制。  

**主要特性**  
- 极速渲染：性能远超 indent-blankline（每帧耗时约 0.15ms vs 2-5ms）。  
- 灵活配置：支持静态缩进线、作用域缩进线、下划线高亮、多颜色渐变等。  
- 兼容性：默认禁用终端、快速修复等非代码文件类型，避免干扰。