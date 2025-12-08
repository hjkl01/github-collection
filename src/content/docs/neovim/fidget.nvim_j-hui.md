
---
title: fidget.nvim
---

### [j-hui fidget.nvim](https://github.com/j-hui/fidget.nvim)

**项目核心内容总结：**

1. **项目功能**  
   Fidget 是 Neovim 的插件，用于显示通知和 LSP（语言服务器协议）进度信息，提供以下功能：  
   - 管理通知（如 LSP 进度、错误提示），支持清除、查看历史记录。  
   - 与 LSP 集成，实时显示语言服务器的进度状态。  
   - 支持通过 Telescope 扩展查看通知历史。  

2. **使用方法**  
   - 安装后通过 Lua API 或 Vim 命令（如 `:Fidget clear`）操作通知。  
   - 配置时可自定义高亮样式（如 `icon_style`）。  
   - 启用 Telescope 扩展需加载 `telescope.nvim` 并调用 `require("telescope").load_extension("fidget")`。  

3. **主要特性**  
   - 支持通过 Lua 脚本和命令行灵活控制通知（如清除、抑制显示）。  
   - 可视化 LSP 进度，集成 LSP 服务器状态更新。  
   - 提供 Telescope 扩展，可过滤和查看通知历史。  
   - 使用内置高亮组，允许用户自定义外观。  

**注意事项**  
- 需要 Neovim 环境及依赖插件（如 Telescope）。  
- LSP 功能需配合语言服务器使用，部分功能依赖 LSP 服务器实现。