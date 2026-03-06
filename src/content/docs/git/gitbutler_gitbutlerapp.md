
---
title: gitbutler
---

### [gitbutlerapp gitbutler](https://github.com/gitbutlerapp/gitbutler)  ![GitHub Repo stars](https://img.shields.io/github/stars/gitbutlerapp/gitbutler?style=social)

GitButler 是一款现代基于 Git 的版本控制系统，提供图形界面和命令行工具，专为 AI 驱动的工作流设计。它可直接集成到现有 Git 仓库中，作为更友好且强大的 Git 用户界面替代品。

主要功能包括：
- **堆叠与并行分支**：支持在分支之上创建堆叠分支，并可并行处理多个分支工作而无需频繁切换。
- **简易提交管理**：支持通过拖拽或命令轻松取消、重命名、修改、移动、拆分和压缩提交，无需交互式变基。
- **撤销时间线**：记录所有操作和变更，支持轻松撤销或恢复任何操作。
- **冲突解决**：支持变基始终成功，提交可标记为冲突并在任意时间按任意顺序解决。
- **Forge 集成**：内置 GitHub/GitLab 集成，可管理拉取请求、分支列表及 CI 状态。
- **AI 工具**：内置 AI 处理程序辅助生成提交信息、分支名和 PR 描述，支持智能体系统钩子。

项目后端基于 Rust 开发，桌面端采用 Tauri 框架。