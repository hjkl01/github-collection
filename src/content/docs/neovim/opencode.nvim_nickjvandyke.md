
---
title: opencode.nvim
---

### [nickjvandyke opencode.nvim](https://github.com/nickjvandyke/opencode.nvim)  ![GitHub Repo stars](https://img.shields.io/github/stars/nickjvandyke/opencode.nvim?style=social)

**项目名称**：opencode.nvim  
**项目简介**：opencode.nvim 是一个 Neovim 插件，用于集成 [opencode](https://github.com/sst/opencode) AI 助手，帮助用户在编辑器中更高效地进行代码研究、审查和请求。

---

### **核心功能**

- **连接任意 opencode 实例**，或使用内置实例
- **共享编辑器上下文**（如当前缓冲区、选区、诊断信息等）
- **输入提示**，支持补全、高亮和普通模式操作
- **选择提示模板**，支持自定义
- **执行命令**
- **实时监控和响应事件**（如编辑、权限请求等）
- **通过 LSP 与 opencode 交互**
- **Vim 风格支持**（如范围操作、点重复）
- **简单默认配置**，开箱即用

---

### **使用方法**

#### **安装（以 lazy.nvim 为例）**
- 添加插件并配置 keymap，推荐使用 `snacks.nvim` 提升交互体验

#### **常用命令**
- `ask()`：向 opencode 输入问题或请求
- `select()`：选择提示或命令
- `prompt()`：发送预定义提示
- `operator()`：支持范围操作的提示
- `command()`：执行 opencode 命令（如 session 控制）

#### **快捷键示例**
- `<C-a>`：询问 opencode
- `<C-x>`：执行 opencode 操作
- `<C-.>`：切换 opencode 状态
- `<S-C-u>` / `<S-C-d>`：滚动 opencode 输出

---

### **主要特性**

- **上下文占位符**：支持 `@this`、`@buffer`、`@diff` 等占位符，自动替换为编辑器内容
- **内置提示模板**：如解释诊断信息、优化代码、添加注释等
- **服务器配置**：可自定义 opencode 启动方式，支持终端或自定义窗口
- **事件处理**：通过 `OpencodeEvent` 处理文件修改、权限请求等
- **状态栏集成**：支持 lualine 显示当前 opencode 状态
- **LSP 支持**（实验性）：通过 LSP 提供 Hover 和 Code Action 功能

---

### **总结**

opencode.nvim 是一个功能强大的 Neovim 插件，它将 opencode AI 助手深度集成到编辑器中，支持上下文感知的代码分析、提示、命令执行和事件处理。通过丰富的 API 和可定制的配置，用户可以高效地进行代码审查、优化和生成，同时保持 Vim 风格的操作习惯。