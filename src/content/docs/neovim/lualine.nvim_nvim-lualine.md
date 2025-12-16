
---
title: lualine.nvim
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/nvim-lualine/lualine.nvim?style=social) ](https://github.com/nvim-lualine/lualine.nvim)
### [nvim-lualine lualine.nvim](https://github.com/nvim-lualine/lualine.nvim)

**项目核心内容总结：**

lualine 是一个用于 Neovim 的插件，用于美化和自定义状态栏（statusline）、标签页（tabline）和窗口栏（winbar）。其核心功能包括：

1. **高度可定制的界面**：通过配置不同组件（如文件名、分支、模式、LSP状态、缓冲区等）实现个性化显示，支持多种组件选项和格式化方式。

2. **多场景支持**：提供标签页（tabline）和窗口栏（winbar）配置功能，可将状态栏内容迁移至标签页或窗口顶部，支持不同窗口的独立显示。

3. **扩展性**：内置多种扩展（如 quickfix、lazy、neo-tree 等），并支持用户自定义扩展，适配其他插件（如 nvim-bufferline、tabline.nvim）。

4. **主题与刷新机制**：支持主题配置，自动定时刷新状态栏内容，也可手动触发刷新（支持延迟刷新或立即刷新）。

5. **便捷操作**：提供跳转缓冲区、重命名标签页、禁用插件等实用功能，支持通过 `:LualineBuffersJump` 等命令快速操作。

**使用方法**：  
- 安装后通过 Lua 配置 `lualine.sections`、`tabline`、`winbar` 等参数，定义各区域的组件组合。  
- 使用 `extensions` 加载预设扩展，或自定义扩展逻辑。  
- 通过 `require('lualine').refresh()` 手动刷新状态栏，或设置 `disabled_filetypes` 禁用特定文件类型的支持。  

**主要特性**：  
- 支持 60+ 内置组件，灵活组合显示信息。  
- 兼容 Neovim 0.8+ 的 winbar 功能，支持活跃/非活跃窗口的不同显示。  
- 提供缓冲区跳转、标签页重命名等交互功能。  
- 通过 `hide()`/`unhide()` 控制插件全局启用/禁用。