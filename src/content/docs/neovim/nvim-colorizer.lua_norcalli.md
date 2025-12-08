
---
title: nvim-colorizer.lua
---

### [norcalli nvim-colorizer.lua](https://github.com/norcalli/nvim-colorizer.lua)

**项目功能**  
`colorizer.lua` 是一个专为 Neovim 设计的高性能颜色高亮插件，支持实时解析并高亮多种颜色格式（如 `#RGB`、`#RRGGBB`、颜色名称等），无需依赖外部工具，性能优异。

**使用方法**  
1. 安装：需 Neovim >= 0.4.0 并启用 `termguicolors`，通过插件管理器（如 `Plug`）或手动克隆至 `runtimepath`。  
2. 配置：通过 `lua require'colorizer'.setup()` 启用，默认为所有文件类型添加高亮；可自定义文件类型、颜色格式及高亮模式（前景/背景）。  

**主要特性**  
- **高性能**：基于 Luajit 实现，支持实时更新，无外部依赖。  
- **灵活定制**：支持多种颜色格式（RGB、HSL、CSS 函数等），可自定义文件类型和高亮模式。  
- **Lua API**：提供接口供用户实现自定义高亮逻辑。  
- **兼容性**：适用于 Linux、macOS、Windows 系统。