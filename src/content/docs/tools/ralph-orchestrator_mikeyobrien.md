
---
title: ralph-orchestrator
---

### [mikeyobrien ralph-orchestrator](https://github.com/mikeyobrien/ralph-orchestrator)  ![GitHub Repo stars](https://img.shields.io/github/stars/mikeyobrien/ralph-orchestrator?style=social)

Ralph Orchestrator 是一个基于“帽子”系统的 AI 代理编排框架，旨在通过持续迭代循环实现任务自动完成。

核心功能：
- **多后端支持**：兼容 Claude、Gemini、Copilot 等多种 AI 工具。
- **角色协调**：通过“帽子”系统（专用角色）与事件机制协调代理工作。
- **质量门控**：集成测试、Lint 和类型检查作为迭代终止条件（Backpressure）。
- **预设模式**：提供 31 种预设（如 TDD、规范驱动、调试）。
- **人机协作**：支持通过 Telegram 进行人类介入（RObot），代理可提问并等待回复。
- **管理界面**：提供 CLI 命令行工具及 Alpha 版 Web 仪表盘用于监控和运行。

技术栈：Rust (后端/CLI) + Node.js (前端)。