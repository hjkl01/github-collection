
---
title: atuin
---

### [atuinsh atuin](https://github.com/atuinsh/atuin)  ![GitHub Repo stars](https://img.shields.io/github/stars/atuinsh/atuin?style=social)

Atuin 是一款增强型 Shell 历史记录工具。它使用 SQLite 数据库替代传统历史文件，记录命令的额外上下文信息（如退出码、执行时长、工作目录、主机名等）。主要功能包括：

1.  **交互式搜索**：提供全屏历史搜索 UI，支持重新绑定 Ctrl-R 和方向键，支持按会话、目录或全局灵活过滤。
2.  **加密同步**：支持可选的端到端加密历史同步，可在不同终端、会话及机器间保持数据一致。
3.  **多 Shell 支持**：兼容 Zsh、Bash、Fish、Nushell、Xonsh 及 PowerShell。
4.  **数据分析**：提供命令统计（如最常用命令）及快速跳转功能，同时保留原有历史文件不被覆盖。