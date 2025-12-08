
---
title: dev-environment-files
---

### [josean-dev dev-environment-files](https://github.com/josean-dev/dev-environment-files)

**项目核心内容总结：**

该README提供一套高度定制化的Mac开发环境配置方案，包含终端、窗口管理、Neovim编辑器及配套工具链。主要功能包括：

1. **终端配置**  
   使用WezTerm替代Alacritty，配套Zsh配置（.zshrc）和主题文件（coolnight.toml），集成fzf、fd、bat等CLI工具提升效率。

2. **窗口管理**  
   支持Yabai（基于Spacebar）和Aerospace（基于Split）两种平铺窗口管理器，包含对应的配置文件（yabairc/skhdrc/aerospace.toml）。

3. **自定义菜单栏**  
   通过Sketchybar实现个性化菜单栏，需安装字体、jq工具及Sketchybar应用字体，配置文件位于.config/sketchybar目录。

4. **Neovim配置**  
   基于lazy.nvim插件管理器，集成LSP、自动补全（nvim-cmp）、语法高亮（treesitter）、代码格式化（conform.nvim）等功能，包含插件列表（如tokyonight主题、telescope模糊搜索、gitsigns等），需安装Neovim 0.9+、iTerm2、Ripgrep等依赖。

**使用方法：**  
- 克隆仓库后替换对应配置文件（如.zshrc、.tmux.conf等）  
- 安装Homebrew并执行依赖安装命令（如brew install neovim、font-meslo等）  
- 根据提示安装语言服务器、插件及字体  

**主要特性：**  
- 支持多窗口管理方案（Yabai/Aerospace）  
- Neovim集成完整开发工具链（LSP、补全、格式化、Git工具）  
- 通过插件提升代码效率（如telescope、lualine状态栏、auto-session会话管理）  
- 配置文件模块化，可按需启用  

**注意事项：**  
配置文件仅供参考，需根据实际需求调整，部分工具依赖Homebrew及特定字体。