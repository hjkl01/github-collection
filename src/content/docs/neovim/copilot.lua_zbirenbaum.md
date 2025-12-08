
---
title: copilot.lua
---

### [zbirenbaum copilot.lua](https://github.com/zbirenbaum/copilot.lua)

**项目核心内容总结：**  
copilot.lua 是一个 Neovim 插件，用于集成 GitHub Copilot 的代码补全功能，支持多种编程语言。其主要特性包括：  
1. **灵活配置**：可通过 `filetypes` 控制启用/禁用特定文件类型，使用 `server_opts_overrides` 自定义 LSP 服务器参数（如补全数量、日志级别）。  
2. **多模式支持**：支持 Node.js 或二进制文件作为语言服务器，可指定自定义路径。  
3. **工作区管理**：通过 `workspace_folders` 提升补全建议的准确性。  
4. **日志与调试**：提供详细的日志记录功能，支持 LSP 消息跟踪及进度日志。  
5. **插件集成**：兼容 `nvim-cmp`、`blink.cmp` 等主流补全框架，以及 `lualine.nvim` 状态栏插件。  

**使用方法**：  
- 安装插件后通过 `:Copilot` 命令操作，支持添加工作区、切换配置等。  
- 配置时通过 Lua 脚本定义 `filetypes`、`server_opts_overrides` 等参数，例如：  
  ```lua  
  require("copilot").setup{  
    filetypes = { javascript = true },  
    server_opts_overrides = { trace = "verbose" }  
  }  
  ```  
- 支持通过 `copilot_node_command` 指定 Node.js 版本路径（需 22+）。