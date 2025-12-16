
---
title: nvim-surround
---

### [kylechui nvim-surround](https://github.com/kylechui/nvim-surround)

**项目功能**  
nvim-surround 是一个 Neovim 插件，用于高效操作文本周围的符号（如括号、引号等），支持添加、删除、修改包围符，提升代码编辑效率。

**主要特性**  
- 一键添加/删除/修改包围符（如函数调用、HTML 标签等）  
- 支持通过 `.` 重复上一次操作  
- 自定义映射和包围符规则  
- 快速跳转到最近的包围符进行修改  
- 单字符别名（如 `q` 代表 `\"'`）简化操作（如 `csqb` 替换引号为括号）  
- 支持用户自定义包围符（兼容 Vim 动作、Lua 正则、Tree-sitter 节点）  
- 高亮选区提供视觉反馈  

**使用方法**  
核心操作通过键位实现：  
- `ys{motion}{char}`：添加包围符（如 `ysiwp` 为单词添加括号）  
- `ds{char}`：删除包围符（如 `ds"` 删除引号）  
- `cs{target}{replacement}`：替换包围符（如 `cs'"` 将引号替换为括号）  

**依赖要求**  
- Neovim 0.8+  
- 推荐安装 [nvim-treesitter-textobjects](https://github.com/nvim-treesitter/nvim-treesitter-textobjects) 以增强配置灵活性  

**安装配置**  
通过插件管理器（如 lazy.nvim 或 packer.nvim）安装后，调用 `require("nvim-surround").setup()` 初始化，默认配置可直接使用。