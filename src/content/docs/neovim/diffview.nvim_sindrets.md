
---
title: diffview.nvim
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/sindrets/diffview.nvim?style=social) ](https://github.com/sindrets/diffview.nvim)
### [sindrets diffview.nvim](https://github.com/sindrets/diffview.nvim)

**diffview.nvim** 是一个基于 Neovim 的插件，用于在 Git 仓库中高效查看文件差异。其核心功能包括：

1. **多视图模式**：支持文件面板、历史记录、选项面板等，可查看 Git 差异、文件历史、配置选项等。
2. **自定义配置**：允许通过 Lua 脚本配置默认行为（如路径排除、缓冲区设置）、快捷键映射、钩子函数（如差异缓冲区初始化、视图打开事件）。
3. **交互操作**：提供快捷键（如 `X` 恢复文件到左侧状态、`<tab>` 切换视图）和命令行参数（如 `-uno` 隐藏未跟踪文件、`--cached` 对比索引与特定版本）。
4. **恢复文件**：通过文件面板的 `X` 键可将文件恢复为左侧差异状态（如 Git 仓库中的历史版本）。
5. **兼容性**：支持 Neovim 的 Lua 配置，集成 Git 命令，适配多种终端（如 Kitty）显示差异的斜线符号。

**使用方法**：通过 `:DiffviewOpen` 命令打开视图，结合参数和快捷键操作差异内容。主要特性包括灵活的视图切换、自定义配置、与 Git 深度集成的文件恢复功能。