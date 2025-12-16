
---
title: any-jump.vim
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/pechorin/any-jump.vim?style=social) ](https://github.com/pechorin/any-jump.vim)
### [pechorin any-jump.vim](https://github.com/pechorin/any-jump.vim)

any-jump.vim 是一款 Vim 插件，用于在 40 多种编程语言中快速查找代码定义和引用位置。它基于 ripgrep 或 ag 等快速正则引擎，支持通过光标位置或手动输入关键字跳转到定义或引用文件。主要功能包括：  
- **定义跳转**：定位变量、类、函数等的定义位置。  
- **引用查找**：显示关键字在代码中的所有使用位置。  
- **多语言支持**：涵盖 Python、Java、JavaScript、Go 等主流语言。  
- **交互式搜索**：支持预览、分屏打开、按文件分组、自定义搜索结果展示等操作。  

使用方法：  
1. 安装插件（如用 vim-plug 添加 `Plug 'pechorin/any-jump.vim'`）。  
2. 在普通或视觉模式下，将光标置于目标符号上按 `<leader>j` 跳转，或执行 `:AnyJump`。  
3. 可通过 `:AnyJumpArg` 手动输入搜索关键字。  

主要特性：  
- 自定义搜索引擎（ripgrep/ag）、忽略文件规则、搜索结果分组方式。  
- 支持 Vim 8.2 及 Neovim 0.4+，提供多种快捷键绑定和 UI 配置选项（如颜色主题、窗口比例、预览行数等）。  
- 可通过设置变量调整行为，例如自动跳转、是否显示行号、结果列表样式等。