
---
title: gitsigns.nvim
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/lewis6991/gitsigns.nvim?style=social) ](https://github.com/lewis6991/gitsigns.nvim)
### [lewis6991 gitsigns.nvim](https://github.com/lewis6991/gitsigns.nvim)

**项目核心内容总结：**

**功能**  
gitsigns.nvim 是一个 Neovim 插件，提供 Git 深度缓冲区集成，用于可视化和操作 Git 差异。主要功能包括：  
- 显示添加、修改、删除代码的符号（支持 staged 和 unstaged 状态区分）。  
- 操作 Git hunk（如 stage/unstage、reset、预览、导航）。  
- 显示当前行或缓冲区的 Git blame 信息（支持虚拟文本、弹窗、命令行）。  
- 支持 diff 比较（可切换基准版本、显示单词级差异）。  
- 集成快速修复列表（Quickfix/Location List）展示 Git 变更。  
- 提供文本对象选择 hunk、状态栏信息集成、多版本缓冲区查看等功能。  

**使用方法**  
- 需 Neovim 0.9+ 和较新 Git 版本。  
- 安装方式：通过包管理器（如 packer.nvim）安装，无需额外配置。  
- 配置：通过 Lua 脚本调用 `require('gitsigns').setup()` 自定义符号、高亮、快捷键等。  
- 快捷键示例：`<leader>hs` stage hunk，`<leader>hr` reset hunk，`[c`/`]c` 导航 hunk，`:Gitsigns blame` 查看 blame 信息。  

**主要特性**  
- 支持 staged/unstaged 状态的符号区分。  
- 提供 hunk 预览（弹窗/内联）、blame 多种展示方式。  
- 可与 trouble.nvim 等插件集成，替代默认的 quickfix 窗口。  
- 支持虚拟文本高亮、自定义快捷键、状态栏信息同步。