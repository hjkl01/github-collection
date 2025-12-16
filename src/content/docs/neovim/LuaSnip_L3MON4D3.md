
---
title: LuaSnip
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/L3MON4D3/LuaSnip?style=social) ](https://github.com/L3MON4D3/LuaSnip)
### [L3MON4D3 LuaSnip](https://github.com/L3MON4D3/LuaSnip)

**项目核心内容总结：**

LuaSnip 是一个用于 Neovim 的代码片段管理插件，支持多种高级功能。  
**主要功能：**  
- 提供标签停靠点、文本转换、条件扩展、嵌套片段、动态片段、正则触发、自动触发、后缀片段等特性；  
- 支持从 VS Code/SnipMate 格式加载片段，或通过 Lua 直接编写复杂片段；  
- 可与 nvim-compe/nvim-cmp 集成，支持片段历史记录及文件类型智能解析（通过 Treesitter）。  

**使用方法：**  
1. **安装：** 使用 Packer/vim-plug/lazy 等插件管理器安装，需 Neovim 0.6+ 及 jsregexp 库（Windows 需额外安装）。  
2. **配置快捷键：** 可通过 Vim 脚本或 Lua 自定义映射（如 `<Tab>` 切换片段选项）。  
3. **加载片段：**  
   - 通过 VS Code/SnipMate 文件加载；  
   - 使用 Lua 脚本调用 `add_snippets` 添加片段；  
   - 推荐使用 Lua 加载器实现热重载及文件跳转功能。  

**特性与注意事项：**  
- 复杂功能需 Lua 编写片段，但大部分场景可用 LSP 语法实现；  
- 配置项支持自动片段触发、删除文本清理等；  
- 官方文档及示例代码详尽，提供中文版教程链接。