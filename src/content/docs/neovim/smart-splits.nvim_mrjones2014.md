
---
title: smart-splits.nvim
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/mrjones2014/smart-splits.nvim?style=social) ](https://github.com/mrjones2014/smart-splits.nvim)
### [mrjones2014 smart-splits.nvim](https://github.com/mrjones2014/smart-splits.nvim)

**核心内容总结：**  
`smart-splits.nvim` 是一个 Neovim 插件，用于统一管理终端多路复用器（如 tmux、wezterm、kitty、zellij）的窗口操作，支持通过快捷键切换窗口、调整大小，无需手动配置每个多路复用器的快捷键。  

**主要功能：**  
- **多平台兼容**：支持 tmux、wezterm、kitty、zellij 等主流终端多路复用器。  
- **统一快捷键**：在 Neovim 中使用统一的键位（如 `Ctrl+hjkl` 切换窗口、`Alt+hjkl` 调整窗口大小）。  
- **API 接口**：提供 Lua API 供脚本调用，支持自定义操作（如获取当前窗口 ID、调整窗口大小等）。  

**使用方法：**  
1. **配置多路复用器**：根据所用工具（如 tmux、kitty 等）添加对应配置代码（如 tmux 的 `bind-key`、kitty 的 `map` 指令）。  
2. **依赖管理**：可结合 `submode.nvim` 实现“持久化调整模式”，通过 `<C-w>r` 进入调整模式，使用方向键调整窗口大小。  
3. **远程操作**：支持通过 Kitty 的 SSH 隧道实现在远程服务器上操作本地多路复用器（需信任远程环境）。  

**主要特性：**  
- 支持自定义快捷键和调整幅度（如 `3` 单位）。  
- 与 `submode.nvim`、`hydra.nvim` 等插件兼容，扩展操作模式。  
- 提供 Lua API 直接调用多路复用器功能（如 `resize_pane`、`split_pane`）。  

**注意事项：**  
- 部分功能（如 Kitty 的 `config.at_edge = 'wrap'`）受限于多路复用器本身能力。  
- 若需懒加载插件，需确保 `IS_NVIM` 用户变量已正确设置（如 Kitty 需在启动时设置）。