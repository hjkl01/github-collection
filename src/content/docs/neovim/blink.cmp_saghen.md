
---
title: blink.cmp
---

### [saghen blink.cmp](https://github.com/saghen/blink.cmp)

**项目核心内容总结：**  
blink.cmp 是一款为 Neovim 设计的高性能补全插件，支持 LSP、命令行、代码片段、签名帮助等功能。其核心特性包括：  
- **开箱即用**：无需额外配置即可使用。  
- **实时更新**：按键时异步更新补全结果（延迟 0.5-4ms）。  
- **模糊匹配**：通过自定义模糊匹配器（Frizbee）提升容错性，支持频率与位置加权。  
- **LSP 支持**：兼容多种语言服务器，提供详细的补全跟踪。  
- **代码片段**：支持 `vim.snippet`、`LuaSnip` 和 `mini.snippets` 等主流插件。  
- **扩展性**：可通过插件源（如 LSP、缓冲区）和组件化渲染实现自定义配置。  
- **其他功能**：自动补全括号、命令行补全、终端补全（需 Neovim 0.11+）。  

**使用方法**：  
通过 [项目文档网站](https://cmp.saghen.dev/installation) 获取安装说明和配置选项。