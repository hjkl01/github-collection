
---
title: agentic.nvim
---

### [carlos-algms agentic.nvim](https://github.com/carlos-algms/agentic.nvim)  ![GitHub Repo stars](https://img.shields.io/github/stars/carlos-algms/agentic.nvim?style=social)

**项目名称**：Agentic.nvim  
**项目简介**：一个在 Neovim 中集成 AI 代理的聊天插件，通过 [Agent Client Protocol (ACP)](https://agentclientprotocol.com) 支持多种 ACP 提供商（如 Claude、Gemini、Codex、Cursor Agent 等）。

---

### ✅ **核心功能**

- **支持多种 ACP 提供商**：Claude、Gemini、Codex、OpenCode、Cursor Agent、Auggie。
- **零配置认证**：无需手动配置 API 密钥，使用终端已配置的认证方式即可。
- **上下文控制**：一键添加文件或代码选区到聊天上下文中。
- **图像支持**：支持拖放或粘贴图像和截图到聊天中。
- **权限系统**：交互式批准 AI 工具调用，支持一键响应。
- **多代理会话**：每个 Neovim 标签页支持独立会话，可同时使用多个代理。
- **简洁 UI**：侧边栏界面，支持 Markdown 渲染和语法高亮。
- **智能上下文**：自动添加系统信息和项目信息到会话开头，节省 AI 分析时间。
- **文件选择器**：输入 `@` 可模糊查找并引用文件。
- **代理模式切换**：支持切换 ACP 提供商支持的代理模式（如默认模式、自动接受模式、计划模式等）。

---

### 🛠 **使用方法**

1. **安装 ACP 提供商 CLI 工具**（需手动安装，推荐使用 `pnpm` 或 `npm`）。
2. **在 Neovim 中配置插件**（推荐使用 `lazy.nvim`）：
   ```lua
   {
     "carlos-algms/agentic.nvim",
     opts = {
       provider = "claude-acp", -- 指定默认的 ACP 提供商
     },
     keys = {
       -- 预设快捷键，例如 Ctrl+\\ 打开聊天
     }
   }
   ```
3. **快捷键使用**：
   - `Ctrl+\\`：打开/关闭聊天窗口。
   - `Ctrl+'`：添加文件或选区到上下文。
   - `Ctrl+,'`：新建会话。

---

### 📦 **依赖与要求**

- **Neovim 版本**：v0.11.0 及以上。
- **ACP CLI 工具**：需手动安装（如 `claude-code-acp`, `gemini-cli` 等）。
- **可选依赖**：`img-clip.nvim` 用于支持图像粘贴功能。

---

### 🧩 **高级配置**

- **自定义 ACP 提供商命令和环境变量**。
- **窗口样式与标题自定义**。
- **快捷键自定义**。
- **事件钩子（如提交提示、响应完成）**。
- **集成 Copilot、lualine、markdown 渲染插件等**。

---

### 🧪 **调试与开发**

- 使用 `:checkhealth agentic` 检查环境是否正常。
- 启用 `debug = true` 查看详细日志（文件路径：`~/.cache/nvim/agentic_debug.log`）。

---

### 📚 **参考资料**

- [Agent Client Protocol 文档](https://agentclientprotocol.com)
- 项目基于 ACP 协议开发，灵感来自多个 Neovim AI 插件。

---

**总结**：Agentic.nvim 是一个功能全面的 AI 代理聊天插件，支持多种 ACP 提供商，提供零配置认证、上下文管理、图像支持、多代理会话等实用功能，适合在 Neovim 中高效使用 AI 工具。