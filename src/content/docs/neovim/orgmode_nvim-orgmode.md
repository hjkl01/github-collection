
---
title: orgmode
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/nvim-orgmode/orgmode?style=social) ](https://github.com/nvim-orgmode/orgmode)
### [nvim-orgmode orgmode](https://github.com/nvim-orgmode/orgmode)

**项目核心内容总结：**

**项目功能**  
nvim-orgmode 是一个用 Lua 编写的 Neovim 插件，提供类似 Emacs Orgmode 的功能，支持任务管理、日程安排、笔记捕获、导出等，适用于 Neovim 0.11.0 及以上版本。

**使用方法**  
1. 安装：推荐使用 `lazy.nvim`，配置示例提供 `orgmode` 初始化代码（如设置议程文件路径）。  
2. 快速操作：  
   - 打开议程：`<Leader>oa`  
   - 捕获笔记：`<Leader>oc`  
   - 缓冲区中按 `g?` 查看帮助。  
3. 文档查看：在线文档地址 [https://nvim-orgmode.github.io](https://nvim-orgmode.github.io)，或在 Neovim 中运行 `:Org help`。

**主要特性**  
- **议程视图**：支持每日/周/月/年视图，按标签、关键字搜索任务，显示截止日期、计划时间、重复任务等。  
- **时间追踪**：支持打卡、统计耗时。  
- **捕获与归档**：自定义模板快速记录，支持归档到文件或添加 `ARCHIVE` 标签。  
- **导出功能**：通过 Emacs、Pandoc 或自定义选项导出内容。  
- **文件操作**：支持调整标题层级、修改 TODO 状态、切换复选框、插入/移动标题、批量处理标签等。  
- **其他**：日历弹窗调整日期、远程编辑、与 `vim-repeat` 插件兼容实现重复映射。  

**依赖与注意事项**  
- 需 Neovim 0.11.0+，安装时若使用 `nvim-treesitter` 需忽略 `org` 语法解析。  
- 不包含 Emacs Orgmode 的扩展插件，功能聚焦于核心功能，扩展需通过独立插件实现。