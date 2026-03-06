
---
title: ralph-claude-code
---

### [frankbria ralph-claude-code](https://github.com/frankbria/ralph-claude-code)  ![GitHub Repo stars](https://img.shields.io/github/stars/frankbria/ralph-claude-code?style=social)

Ralph 是基于 Claude Code 的自主 AI 开发循环工具，旨在实现项目的持续迭代直至完成。

核心功能：
1. **自主开发循环**：自动运行 Claude Code 持续改进项目代码。
2. **智能退出检测**：采用双条件检查（完成指示 + 显式 EXIT_SIGNAL）防止过早终止或无限循环。
3. **安全机制**：内置 API 速率限制、熔断器（防止错误死循环）及 5 小时使用限制处理。
4. **灵活部署**：一次全局安装，支持现有项目启用（交互式向导）、PRD 文档导入或新建项目初始化。
5. **会话与监控**：支持跨迭代会话延续、实时输出流、tmux 集成监控及 `.ralphrc` 配置管理。
6. **工程化工具**：提供 CI/CD 集成、版本迁移、日志管理及完整卸载脚本。

当前状态：v0.11.5，活跃开发中，测试覆盖率 100%。