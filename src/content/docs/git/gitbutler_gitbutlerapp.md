
---
title: gitbutler
---

### [gitbutlerapp gitbutler](https://github.com/gitbutlerapp/gitbutler)  ![GitHub Repo stars](https://img.shields.io/github/stars/gitbutlerapp/gitbutler?style=social)

GitButler 是一款专为 AI 工作流设计的现代化 Git 版本控制系统，提供 GUI 和 CLI，可无缝作为现有 Git 仓库的增强型替代品。

核心功能：
- **堆叠与并行分支**：支持创建堆叠分支，并行管理多分支工作，无需频繁切换。
- **便捷提交管理**：支持撤回、重写、修改、移动、拆分和压缩提交，无需使用复杂的 `rebase -i`。
- **操作时间线**：记录所有操作历史，支持轻松撤销或恢复任何更改。
- **原生冲突处理**：确保变基始终成功，允许随时标记和解决冲突。
- **代码托管集成**：集成 GitHub 和 GitLab，直接管理 Pull Request、分支列表及 CI 状态。
- **AI 工具集成**：内置 AI 助手生成提交信息、分支名称和 PR 描述，支持 Agent 系统 Hooks。

技术实现：桌面端基于 Tauri（Rust 后端，Svelte/TypeScript 前端），CLI 使用相同的 Rust 引擎。