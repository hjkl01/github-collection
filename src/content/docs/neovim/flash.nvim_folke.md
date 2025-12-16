
---
title: flash.nvim
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/folke/flash.nvim?style=social) ](https://github.com/folke/flash.nvim)
### [folke flash.nvim](https://github.com/folke/flash.nvim)

**flash.nvim** 是一个用于 Neovim 的快速跳转插件，支持基于字符、单词、行等的精准定位，功能类似 Leap 或 Hop。核心特性包括：  
1. **跳转方式**：通过 `f/t` 命令实现标签跳转，支持自定义搜索模式（如正则、单词边界）；可跳转至行、单词、符号等。  
2. **交互提示**：提供实时高亮匹配项，支持键盘输入过滤结果，跳转前可预览目标位置。  
3. **扩展性**：支持与 Telescope、Snacks Picker 等插件集成，实现搜索结果中标记跳转；允许自定义匹配逻辑（如结合 LSP 诊断信息）。  
4. **高亮与样式**：提供多组高亮主题（如匹配项、当前项、标签等），支持自定义颜色和格式。  
5. **高级功能**：支持多标签跳转、继续上次搜索、增量选择（需配合 Treesitter）等。  

**使用方法**：通过 Lua 配置插件选项，绑定快捷键（如 `f`/`t`）触发跳转；可结合 `pattern` 参数指定初始匹配内容，或通过 `continue` 参数延续上一次搜索。