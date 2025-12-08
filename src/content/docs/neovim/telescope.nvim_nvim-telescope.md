
---
title: telescope.nvim
---

### [nvim-telescope telescope.nvim](https://github.com/nvim-telescope/telescope.nvim)

**项目功能**  
telescope.nvim 是一个 Neovim 插件，用于快速查找和管理文件、修改历史、书签、命令历史等，支持多种搜索方式（如模糊搜索、正则匹配）和扩展功能（如集成外部工具）。  

**使用方法**  
通过 Vim 命令（如 `:Telescope find_files`）或 Lua 脚本调用内置的 picker（如 `find_files`、`live_grep`），支持自定义布局、主题、排序规则等参数。  

**主要特性**  
1. **灵活布局**：支持垂直、水平、覆盖等布局策略，可自定义窗口大小和位置。  
2. **主题自定义**：提供下拉菜单、光标相对列表等主题，支持 winblend、高亮等配置。  
3. **扩展性**：可通过加载扩展（如 `fzy_native`）增强功能，或开发自定义 picker。  
4. **高效搜索**：内置多种排序算法（如模糊匹配、Levenshtein 距离），支持实时搜索和历史记录。  
5. **自动化集成**：支持用户自定义 autocmd 事件（如窗口创建后操作）。