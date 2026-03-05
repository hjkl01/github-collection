
---
title: claude-code-hooks-mastery
---

### [disler claude-code-hooks-mastery](https://github.com/disler/claude-code-hooks-mastery)  ![GitHub Repo stars](https://img.shields.io/github/stars/disler/claude-code-hooks-mastery?style=social)

该项目是一个 Claude Code Hooks 的全功能实战框架，旨在提供对 Claude Code 行为的确定性控制与体验增强。

**核心功能：**
1.  **钩子生命周期全覆盖**：实现全部 13 个钩子事件（包括提示提交、工具执行、会话管理、子代理等），支持提示验证、危险命令拦截、错误审计及自动化日志记录。
2.  **安全与流程控制**：通过钩子逻辑阻断危险操作，验证工具结果，管理权限请求，并支持结构化 JSON 输出控制执行流。
3.  **增强体验**：集成 TTS 语音反馈系统，提供多种自定义终端状态线（显示成本、Token、Git 信息等）及多种响应输出样式（HTML、表格、YAML 等）。
4.  **代理协作系统**：支持 Claude Code 子代理（Sub-Agents）架构，包含团队验证模式（构建者/验证者）、元代理（自动生成代理）及任务编排。
5.  **架构设计**：基于 UV 单文件 Python 脚本构建钩子，确保逻辑隔离、依赖管理及跨环境便携性。