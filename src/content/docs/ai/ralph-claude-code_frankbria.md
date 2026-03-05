
---
title: ralph-claude-code
---

### [frankbria ralph-claude-code](https://github.com/frankbria/ralph-claude-code)  ![GitHub Repo stars](https://img.shields.io/github/stars/frankbria/ralph-claude-code?style=social)

Ralph for Claude Code 是一个基于 Claude Code 的自主 AI 开发循环工具，实现了 Geoffrey Huntley 的 Ralph 技术。它使 AI 能在项目中持续迭代改进直至完成，同时具备防止无限循环和 API 滥用的安全机制。

核心功能：
1. **自主开发循环**：自动执行开发任务，持续优化项目。
2. **智能退出检测**：双重条件检查（完成指标 + 显式信号）防止过早退出。
3. **安全限流**：内置 API 速率限制、5 小时限额处理及电路断路器。
4. **会话管理**：支持上下文保持、超时重置及手动刷新。
5. **任务配置**：支持 PRD 导入、交互式启用向导及 `.ralphrc` 配置。
6. **监控可视化**：集成 tmux 实时监控、实时流输出及日志追踪。
7. **全局可用**：安装一次后提供全局命令，支持任意目录使用。

当前版本 v0.11.5，测试通过率 100%，处于活跃开发中。