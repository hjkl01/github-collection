
---
title: fzf-lua
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/ibhagwan/fzf-lua?style=social) ](https://github.com/ibhagwan/fzf-lua)
### [ibhagwan fzf-lua](https://github.com/ibhagwan/fzf-lua)

**项目核心内容总结：**

**功能**  
fzf-lua 是一个基于 Neovim 的模糊搜索插件，集成 fzf 的强大功能，支持文件、缓冲区、标签、命令等多场景搜索，提供实时 LSP 符号查询和内置预览窗口，可高度自定义界面和交互。

**使用方法**  
1. 安装插件后，通过 `setup` 配置文件定义基础参数（如颜色方案、快捷键）。  
2. 使用预设命令（如 `:Files`、`:Buffers`）触发搜索，或通过自定义命令扩展功能。  
3. 支持在搜索时动态调整配置，例如通过 `fzf_colors = true` 自动生成与 Neovim 配色匹配的 fzf 颜色方案。

**主要特性**  
- **多界面支持**：文件、缓冲区、标签、命令、LSP 符号等场景的模糊搜索。  
- **高度可定制**：通过 `hls`（高亮配置）和 `fzf_colors` 自定义颜色、字体样式及交互逻辑。  
- **内置预览器**：支持文件内容、缓冲区信息、路径格式化等预览。  
- **实时 LSP 集成**：输入时动态显示当前文件的 LSP 符号匹配结果。  
- **快捷键绑定**：可自定义搜索界面的快捷键（如 `q` 退出、`Enter` 选择）。  
- **兼容性**：兼容 fzf.vim 的 `g:fzf_colors` 配置，支持 Neovim 高亮组与原始 fzf 颜色参数混合使用。