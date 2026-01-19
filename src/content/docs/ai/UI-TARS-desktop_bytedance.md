
---
title: UI-TARS-desktop
---

### [bytedance UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop)  ![GitHub Repo stars](https://img.shields.io/github/stars/bytedance/UI-TARS-desktop?style=social)

**项目核心内容总结：**

**Agent TARS** 是一个基于 MCP（Model-Cloud-Proxy）框架的自动化工具，支持通过自然语言指令控制计算机操作（如文件管理、软件设置等）。其核心功能包括：
- **多模型支持**：兼容 Volcengine、Anthropic 等多家模型提供商（如 Claude、Doubao 等）。
- **事件驱动架构**：通过 MCP 与现实工具（如 VS Code、GitHub）交互，实现精准的鼠标/键盘控制。
- **本地处理**：所有操作在本地完成，保障隐私与安全性。

**使用方法**：
1. 安装：`npx @agent-tars/cli@latest` 或全局安装 `npm install -g @agent-tars/cli`。
2. 运行：指定模型提供商及 API 密钥，例如 `agent-tars --provider volcengine --model doubao-1-5-thinking-vision-pro-250428 --apiKey your-api-key`。

**主要特性**：
- 支持跨平台（Windows/MacOS/Browser）。
- 实时反馈操作状态。
- 可集成 MCP 服务器扩展功能。

---

**UI-TARS Desktop** 是 Agent TARS 的本地 GUI 版本，基于 Seed-1.5-VL/1.6 视觉语言模型，提供以下能力：
- **自然语言控制**：通过视觉识别与鼠标/键盘操作实现复杂任务（如修改 VS Code 设置、查询 GitHub 项目问题）。
- **跨平台支持**：兼容 Windows、MacOS 及浏览器（通过 Midscene）。
- **本地隐私保护**：所有数据处理在本地完成，无云端传输。

**使用方法**：参考项目文档中的 [Quick Start](./docs/quick-start.md)。