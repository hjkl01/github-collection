
---
title: opencode.nvim
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/NickvanDyke/opencode.nvim?style=social) ](https://github.com/NickvanDyke/opencode.nvim)
### [NickvanDyke opencode.nvim](https://github.com/NickvanDyke/opencode.nvim)

**项目核心内容总结**  

`opencode.nvim` 是一个将 AI 助手 `opencode` 集成到 Neovim 的插件，用于代码审查、研究和请求。其核心功能包括：  
- **自动连接**：自动连接当前目录运行的 `opencode` 实例，或提供内置实例。  
- **交互支持**：支持提示输入（带补全和高亮）、预定义提示库（如解释诊断、优化代码等）、编辑器上下文注入（如光标位置、选中内容、诊断信息等）。  
- **实时协作**：实时重载 `opencode` 编辑的文件，监控其状态（如通过状态栏组件）。  
- **事件与命令**：转发 `opencode` 的事件为 Neovim 自定义命令（如滚动、中断会话），支持权限请求交互。  

**使用方法**  
- **配置**：通过 `lazy.nvim` 或 `nixvim` 安装，配置提供者（如 `snacks`、`kitty`、`wezterm` 等终端工具）和快捷键（如 `<C-a>` 提问、`<C-x>` 选择操作）。  
- **交互命令**：使用 `ask()` 提问、`select()` 选择操作、`prompt()` 触发预定义提示、`command()` 执行会话控制（如滚动、中断）。  
- **事件处理**：通过 `OpencodeEvent` 自定义命令监听 `opencode` 的事件（如会话完成通知）。  

**主要特性**  
- 提供默认配置，支持灵活自定义（如上下文占位符替换规则、提示库定义）。  
- 支持多种终端提供者，允许自定义集成方法。  
- 实时响应文件修改、权限请求，提升协作效率。