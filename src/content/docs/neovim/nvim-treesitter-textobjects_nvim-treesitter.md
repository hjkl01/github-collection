
---
title: nvim-treesitter-textobjects
---

### [nvim-treesitter nvim-treesitter-textobjects](https://github.com/nvim-treesitter/nvim-treesitter-textobjects)  ![GitHub Repo stars](https://img.shields.io/github/stars/nvim-treesitter/nvim-treesitter-textobjects?style=social)

nvim-treesitter-textobjects 是一款基于 Tree-sitter 的 Neovim 插件，提供语法感知的文本对象操作。

核心功能：
1. **选择（Select）**：支持自定义文本对象（如函数、类、参数）的选择，可配置字符/行/块选择模式及是否包含周围空白。
2. **交换（Swap）**：允许交换光标下节点与前后相邻节点（如函数参数）。
3. **移动（Move）**：支持在各类文本对象间跳转（函数、类、循环、作用域等），可配置跳转起止位置，支持自定义重复移动快捷键（; 和 ,），并增强内置查找命令的重复性。
4. **扩展（Extend）**：支持通过 query 文件覆盖或添加自定义捕获组来扩展文本对象。

说明：该功能依赖 Neovim 的 Tree-sitter 支持，目前属于实验性功能。