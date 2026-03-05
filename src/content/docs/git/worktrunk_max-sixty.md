
---
title: worktrunk
---

### [max-sixty worktrunk](https://github.com/max-sixty/worktrunk)  ![GitHub Repo stars](https://img.shields.io/github/stars/max-sixty/worktrunk?style=social)

Worktrunk 是一款基于 Rust 的 Git Worktree 管理命令行工具 (CLI)，专为并行运行 AI 代理设计。它将 Worktree 按分支名称寻址并自动计算路径，使操作如同分支切换般简便，解决了原生 Git Worktree 命令繁琐的问题。核心功能包括便捷的创建、切换和清理命令，支持钩子脚本、LLM 生成提交信息、智能合并流程、交互式选择器及构建缓存共享等自动化工作流。该工具支持在多个 Worktree 中并行启动 AI 代理，大幅降低了多任务并行开发的复杂度。