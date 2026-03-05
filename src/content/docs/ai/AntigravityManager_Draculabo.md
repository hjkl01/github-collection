
---
title: AntigravityManager
---

### [Draculabo AntigravityManager](https://github.com/Draculabo/AntigravityManager)  ![GitHub Repo stars](https://img.shields.io/github/stars/Draculabo/AntigravityManager?style=social)

Antigravity Manager 是一款基于 Electron 开发的跨平台桌面应用，专为 Google Gemini 和 Claude AI 提供多账户管理解决方案。

**核心功能：**
*   **无限账户池**：支持通过 OAuth 添加任意数量账户，实时显示头像、邮箱及账户状态（活跃、限流、过期）。
*   **智能自动切换**：当账户配额不足（<5%）或遭遇限流时，自动无缝切换至备用账户。
*   **实时额度监控**：可视化展示各模型（如 gemini-pro, claude-3-5-sonnet）的剩余配额及进度条。
*   **本地 API 代理**：内置兼容 OpenAI 和 Anthropic 规范的本地服务器，支持端口配置与模型映射。
*   **安全与备份**：敏感数据采用 AES-256-GCM 加密，支持账户状态快照、批量操作及 IDE 数据同步导入。
*   **辅助工具**：支持系统托盘运行、IDE 进程控制（启动/关闭）、API 代码生成及多语言界面。

**适用平台**：Windows、macOS、Linux。
**许可声明**：CC BY-NC-SA 4.0，仅供教育和研究用途，禁止商业使用。