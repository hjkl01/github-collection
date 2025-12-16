
---
title: neo-tree.nvim
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/nvim-neo-tree/neo-tree.nvim?style=social) ](https://github.com/nvim-neo-tree/neo-tree.nvim)
### [nvim-neo-tree neo-tree.nvim](https://github.com/nvim-neo-tree/neo-tree.nvim)

### 核心内容总结

**项目功能**  
`neo-tree.nvim` 是一个为 Neovim 设计的文件树管理插件，支持多种文件源（如本地文件系统、书签、Harpoon 等），提供灵活的自定义功能，包括节点渲染、预览模式、源切换等。  

**使用方法**  
1. **安装**：通过 Lua 配置文件调用 `require("neo-tree").setup()` 进行初始化。  
2. **命令**：使用 `:Neotree` 打开/关闭文件树，支持参数（如 `:Neotree file` 从当前文件打开）。  
3. **配置**：通过 Lua 表配置树样式、映射、源选择器（winbar/statusline）、预览模式等。  

**主要特性**  
- **高度可定制**：支持自定义节点渲染器、组件函数、事件钩子（如 `before_render`）。  
- **多源支持**：集成文件系统、书签、Harpoon 等，支持外部源扩展。  
- **预览模式**：无需切换焦点即可预览文件（支持图片渲染，依赖 `snacks.nvim` 或 `image.nvim`）。  
- **源选择器**：通过 winbar 或 statusline 切换不同文件源。  
- **稳定性**：遵循语义化版本控制，重大变更前会提示弃用。  
- **依赖库**：基于 `nui.nvim` 和 `plenary.nvim` 实现，提升可维护性和功能扩展性。