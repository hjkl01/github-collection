
---
title: inc-rename.nvim
---

### [smjonas inc-rename.nvim](https://github.com/smjonas/inc-rename.nvim)

**项目核心内容总结：**

**功能**：  
`inc-rename.nvim` 是一个 Neovim 插件，提供 LSP 重命名功能，并通过 Neovim 的命令预览功能实现实时视觉反馈，提升重命名操作的效率和体验。

**使用方法**：  
1. 安装插件（支持 `lazy.nvim`、`packer.nvim`、`vim-plug`）。  
2. 调用 `:IncRename <新名称>` 命令，或通过自定义快捷键（如 `<leader>rn`）触发。  
3. 支持通过 `dressing.nvim` 或 `snacks.nvim` 实现输入框的交互优化。  

**主要特性**：  
- 实时预览重命名效果，无需等待操作完成。  
- 兼容 `noice.nvim`、`dressing.nvim`、`snacks.nvim` 等插件，增强交互体验。  
- 可自定义命令名称、高亮样式、是否保存命令历史等选项。  

**注意事项**：  
- 与 `traces.vim`、`custom-elements-languageserver` 等插件可能存在兼容性问题，需注意排查。  
- 多文件重命名时需确保已保存相关缓冲区（`:wa`）。