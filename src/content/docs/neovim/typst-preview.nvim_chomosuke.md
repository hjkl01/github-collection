
---
title: typst-preview.nvim
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/chomosuke/typst-preview.nvim?style=social) ](https://github.com/chomosuke/typst-preview.nvim)
### [chomosuke typst-preview.nvim](https://github.com/chomosuke/typst-preview.nvim)

### 核心内容总结

**项目功能**  
这是一个为 Neovim 设计的插件，用于实时预览 Typst 文档，支持代码与预览的双向跳转，依赖于 `tinymist` 工具。  

**主要特性**  
- **低延迟预览**：基于增量渲染技术，实现近乎实时的文档预览。  
- **代码与预览跳转**：点击预览区域可跳转至对应代码位置，且预览可跟随光标移动。  
- **自定义配置**：支持设置调试模式、颜色反转、跟随光标行为、依赖项路径等。  

**使用方法**  
1. **安装**：通过 Lazy.nvim、Packer.nvim 或 vim-plug 安装插件，并调用 `setup {}` 初始化（会自动下载所需二进制文件）。  
2. **命令操作**：  
   - `:TypstPreview` 启动预览（可选文档或幻灯片模式）。  
   - `:TypstPreviewStop` 停止预览。  
   - `:TypstPreviewToggle` 切换预览状态。  
   - `:TypstPreviewFollowCursor` 控制预览是否跟随光标。  

**配置选项**  
- 默认配置包含调试日志、颜色反转、依赖项路径、项目根目录获取函数等，用户可通过 `setup` 函数自定义。  
- 支持通过 Mason 安装的 `tinymist` 工具路径。  

**注意事项**  
- 需确保系统安装 `curl` 以下载依赖。  
- 若使用 `typst-lsp` 相关工具，需注意其可能存在的延迟及不支持跳转的问题。