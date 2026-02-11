
---
title: nvim-dap-view
---

### [igorlfs nvim-dap-view](https://github.com/igorlfs/nvim-dap-view)  ![GitHub Repo stars](https://img.shields.io/github/stars/igorlfs/nvim-dap-view?style=social)

**nvim-dap-view 简介**

**项目功能：**  
nvim-dap-view 是一个轻量级的 Neovim 调试插件，用于替代 nvim-dap-ui。它提供统一的窗口来管理调试会话，支持查看变量、设置断点、浏览调用栈、表达式监视和 REPL 功能。

**主要特性：**  
- 查看变量和表达式  
- 管理断点  
- 浏览调用栈  
- 管理调试会话  
- 使用 REPL 进行交互  
- 支持通过快捷键切换调试视图部分（如 `B` 切换断点）  
- 支持高度自定义  

**使用方法：**  
1. 启动一个调试会话。  
2. 输入 `:DapViewOpen` 打开插件窗口。  
3. 使用 `g?` 查看当前区域的快捷键。  
4. 使用 `:DapViewClose` 关闭插件。  

**安装方式（lazy.nvim 示例）：**  
```lua
return {
    {
        "igorlfs/nvim-dap-view",
        ---@module 'dap-view'
        ---@type dapview.Config
        opts = {},
    },
}
```

**要求：**  
- 需要 Neovim 0.11 或以上版本。