
---
title: nvim-treesitter
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/nvim-treesitter/nvim-treesitter?style=social) ](https://github.com/nvim-treesitter/nvim-treesitter)
### [nvim-treesitter nvim-treesitter](https://github.com/nvim-treesitter/nvim-treesitter)

**项目核心内容总结：**

**功能**  
为 Neovim 提供基于 Tree-sitter 的语法高亮、文本对象定位、代码折叠等功能，支持多种编程语言。用户可通过自定义查询、模块扩展实现高级功能（如注入、符号跳转等）。

**使用方法**  
1. **安装**：通过 `:TSInstall` 安装语言解析器，或手动配置 Git/curl 下载。  
2. **配置**：在 `init.lua` 中调用 `require'nvim-treesitter.configs'.setup` 启用模块（如高亮、折叠）。  
3. **自定义**：添加查询文件（如 `queries/highlights.scm`）或编写模块，通过 `define_modules` 注册功能。  

**主要特性**  
- **模块化架构**：支持独立启用/禁用功能（如高亮、文本对象），兼容第三方模块。  
- **查询系统**：通过 `.scm` 文件定义规则，支持继承、覆盖默认查询。  
- **扩展性**：允许注册自定义语言文件类型（如 `vim.treesitter.language.register`），适配非标准文件格式。  
- **调试工具**：提供 `:checkhealth` 检查依赖、`TSBufEnable` 修复高亮异常等实用命令。  

**注意事项**  
- 确保 Neovim 版本支持 Tree-sitter（v0.9+）。  
- 若遇到查询错误，需更新解析器（`:TSUpdate`）或检查 `filetype` 配置。