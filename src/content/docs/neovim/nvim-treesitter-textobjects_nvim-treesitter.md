
---
title: nvim-treesitter-textobjects
---

### [nvim-treesitter nvim-treesitter-textobjects](https://github.com/nvim-treesitter/nvim-treesitter-textobjects)  ![GitHub Repo stars](https://img.shields.io/github/stars/nvim-treesitter/nvim-treesitter-textobjects?style=social)

`nvim-treesitter-textobjects` 是一款基于 tree-sitter 的 Neovim 插件，提供语法感知（Syntax aware）的文本对象操作。核心功能包括：
1. **选择**：支持自定义文本对象（如函数、类）的内/外选择，可配置选择模式、前瞻跳转及周围空白处理。
2. **交换**：支持交换光标节点与相邻节点（如函数参数）。
3. **移动**：支持跳转到下一个或上一个文本对象，集成跳转列表，并支持通过 `;` 和 `,` 重复移动。

插件支持通过查询文件（scm）扩展或覆盖文本对象，内置支持多种语言的文本对象捕获组。