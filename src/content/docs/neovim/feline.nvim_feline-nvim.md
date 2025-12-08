
---
title: feline.nvim
---

### [feline-nvim feline.nvim](https://github.com/feline-nvim/feline.nvim)

**项目核心内容总结：**

**功能**  
feline.nvim 是一个为 Neovim 设计的 Lua 状态栏（statusline）和窗口栏（winbar）插件，提供极简、美观且高度可定制的界面。支持内置多种信息模块（如 Vi 模式、文件信息、诊断信息、Git 状态等），并允许用户自由组合和扩展功能。

**使用方法**  
1. **安装**：通过插件管理器（如 packer.nvim 或 vim-plug）安装，兼容 Neovim 0.5 及以上版本（需启用 `termguicolors`）。  
2. **初始化**：调用 `require('feline').setup()` 即可使用默认配置；如需启用 winbar，补充 `require('feline').winbar.setup()`。  
3. **自定义**：通过 Lua 配置文件修改组件布局、样式及功能，详细用法见项目文档。

**主要特性**  
- **高度可定制**：用户可完全控制每个组件的位置、外观及内容，支持自定义提供者（provider）。  
- **轻量高效**：模块延迟加载，启动和更新速度快，资源占用低。  
- **兼容性强**：提供针对旧版 Neovim 的兼容分支（如 `0.5-compat`）。  
- **文档完善**：提供详细配置示例和帮助文档，降低学习成本。  

**依赖要求**  
- Neovim 0.5+（推荐 0.7+）；  
- 可选依赖：`nvim-web-devicons`（图标支持）、`gitsigns.nvim`（Git 状态信息）。