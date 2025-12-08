
---
title: neogen
---

### [danymat neogen](https://github.com/danymat/neogen)

**核心内容总结：**  
Neogen 是一款基于 Neovim 的注释生成工具，使用 Lua 编写并集成 Tree-sitter。其主要功能包括：  
1. **多语言支持**：涵盖 Python、JavaScript、Ruby、Java 等 20+ 语言，每种语言支持多种注释规范（如 Google docstrings、JSDoc、KDoc 等）。  
2. **灵活使用方式**：通过命令 `:Neogen` 或 Lua API 的 `generate` 函数生成注释，支持自定义快捷键（如 `<Leader>nf` 生成函数注释）。  
3. **高度可定制**：支持代码片段引擎（如 luasnip、snippy）生成注释，或使用原生跳转功能在注释字段间移动。  
4. **扩展性**：提供文档指导用户添加新语言支持，便于扩展功能。  
5. **辅助功能**：包含测试用例、开发文档（`:h neogen-develop`）及社区支持。  

**使用方法**：  
- 安装后通过 `:Neogen` 命令或 Lua 脚本调用 `generate` 函数生成注释。  
- 配置代码片段引擎或使用原生跳转功能优化注释编辑体验。  
- 通过文档学习如何添加新语言支持。