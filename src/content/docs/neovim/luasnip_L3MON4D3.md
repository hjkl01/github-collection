
---
title: luasnip
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/L3MON4D3/luasnip?style=social) ](https://github.com/L3MON4D3/luasnip)
### [L3MON4D3 luasnip](https://github.com/L3MON4D3/luasnip)

**项目功能**  
LuaSnip 是一款为 Neovim 设计的代码片段插件，支持通过 SnipMate、VS Code 格式或 Lua 脚本定义片段，提供动态内容生成、自动补全、跳转定义文件等功能，适用于多种编程语言。

**使用方法**  
1. 安装插件后，通过 `add_snippets` 加载 Lua 编写的片段，或使用 SnipMate/VS Code 格式片段。  
2. 配置 Neovim 的 `region_check_events`、`delete_check_events` 等选项，启用自动补全或热重载。  
3. 使用 `:help luasnip.txt` 或官方文档查看 API 和示例片段。

**主要特性**  
- 支持 SnipMate、VS Code 格式片段，兼容性强；  
- 提供 `functionNode`、`dynamicNode` 等高级节点，支持复杂逻辑；  
- 支持热重载（同一 Neovim 实例内）和跳转至定义文件；  
- 附带丰富文档、示例代码及教程资源（如 TJ DeVries 的视频）。