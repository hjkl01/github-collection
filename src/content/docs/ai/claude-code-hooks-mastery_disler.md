
---
title: claude-code-hooks-mastery
---

### [disler claude-code-hooks-mastery](https://github.com/disler/claude-code-hooks-mastery)  ![GitHub Repo stars](https://img.shields.io/github/stars/disler/claude-code-hooks-mastery?style=social)

本项目是一套完整的 Claude Code Hooks 增强方案，核心功能包括：

1.  **Hook 生命周期管理**：实现全部 13 种钩子事件，支持日志记录、安全拦截（如阻断危险命令）、上下文注入及执行流控制。
2.  **代理协作系统**：支持专用子代理、Meta-Agent（自动创建代理）及团队验证模式（构建者/验证者），实现任务分配与代码质量审计。
3.  **增强交互体验**：集成 TTS 语音反馈、自定义终端状态行、多风格输出及自定义命令。
4.  **架构与日志**：基于 UV 单文件脚本隔离依赖，全量记录 JSON 日志以支持审计与可追溯性。