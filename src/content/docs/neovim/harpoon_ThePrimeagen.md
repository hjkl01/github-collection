
---
title: harpoon
---

### [ThePrimeagen harpoon](https://github.com/ThePrimeagen/harpoon)

**核心内容总结：**  
Harpoon 是一个 Neovim 插件，用于快速导航常用文件和管理终端。主要功能包括：  
- **文件标记**：通过快捷键标记文件，快速跳转至常用文件，支持自动更新标记位置。  
- **终端管理**：创建持久化终端会话，执行项目相关命令，支持 Tmux 集成。  
- **自定义配置**：可自定义命令、标签样式，支持 Telescope 插件搜索文件。  
- **项目级保存**：标记和配置按项目保存，便于多项目切换。  
- **日志记录**：支持调试日志，便于问题排查。  

**使用方法**：  
1. 安装需 Neovim 0.5.0+ 和插件管理器（如 vim-plug）。  
2. 使用 `:lua require("harpoon.mark").add_file()` 标记文件。  
3. 通过快捷键或命令跳转文件，管理终端会话。  

**注意事项**：  
- Harpoon 2 已弃用，未来更新在 `harpoon2` 分支。  
- 需依赖 Lua 环境及 Neovim 0.5.0+。  
- 遇到问题可通过 Discord、Twitch 等渠道联系作者。