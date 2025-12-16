
---
title: formatter.nvim
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/mhartington/formatter.nvim?style=social) ](https://github.com/mhartington/formatter.nvim)
### [mhartington formatter.nvim](https://github.com/mhartington/formatter.nvim)

**项目核心内容总结：**  
Formatter.nvim 是一个为 Neovim 设计的代码格式化工具，支持异步执行、缓冲区锁定、条件格式化等功能。用户可通过 Lua 配置格式化规则，支持多种文件类型（如 Lua、JavaScript 等）的默认格式化方案，并允许自定义配置。  

**主要特性：**  
- 异步执行格式化操作，提升效率  
- 缓冲区锁定机制防止格式化时内容被修改  
- 支持按文件类型（如 Lua）或通用规则（`*`）配置格式化器  
- 提供“格式化前/后”钩子（Hook）执行自定义逻辑  
- 支持条件格式化（如根据文件名动态选择规则）  

**使用方法：**  
1. **安装**：支持 Packer、Vim-Plug 等主流插件管理器安装。  
2. **配置**：通过 Lua 脚本定义格式化规则，例如：  
   ```lua  
   require("formatter").setup {  
     filetype = {  
       lua = { require("formatter.filetypes.lua").stylua },  
       ["*"] = { require("formatter.filetypes.any").remove_trailing_whitespace }  
     }  
   }  
   ```  
3. **快捷键映射**：绑定 `Format`（格式化当前内容）和 `FormatWrite`（保存时自动格式化）命令。  
4. **自动触发**：通过 `BufWritePost` 自动触发保存后格式化。  

**注意事项：**  
- 默认无预设格式化器，需手动启用或自定义配置。  
- 支持通过 `transform` 函数对格式化结果进行二次处理（如 Ruby 的 Rubocop 配置示例）。