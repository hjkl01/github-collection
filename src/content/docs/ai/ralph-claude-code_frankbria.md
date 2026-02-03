
---
title: ralph-claude-code
---

### [frankbria ralph-claude-code](https://github.com/frankbria/ralph-claude-code)  ![GitHub Repo stars](https://img.shields.io/github/stars/frankbria/ralph-claude-code?style=social)

**项目核心内容总结：**

Ralph 是一个基于 Claude Code 的 AI 编码助手自动化工具，用于自动执行代码生成、项目构建等任务。其核心功能包括：  
1. **自动化任务执行**：通过循环调用 Claude Code 生成代码，结合智能退出机制（根据任务完成度和 Claude 返回的 `EXIT_SIGNAL` 判断是否终止）。  
2. **监控与调试**：集成 tmux 实时监控面板，显示 API 调用次数、日志、循环状态等；支持查看日志、调整超时时间、重置会话等操作。  
3. **资源管理**：内置速率限制（默认每小时 100 次调用）、5 小时 API 使用限制检测、会话生命周期管理（自动重置过期会话）。  
4. **项目初始化与导入**：提供 `ralph-setup` 创建新项目，`ralph-import` 导入 PRD/需求文档生成 Ralph 项目结构。  
5. **测试与稳定性**：通过 308 个单元和集成测试（100% 通过率），覆盖 CLI 命令、JSON 解析、退出逻辑、安装流程等场景。  

**使用方法**：  
- 安装：运行 `./install.sh`。  
- 启动：使用 `ralph` 命令，支持 `--monitor`（开启 tmux 监控）、`--timeout`（设置超时时间）、`--calls`（限制调用次数）等参数。  
- 项目操作：通过 `ralph-setup` 创建项目，`ralph-import` 导入需求文档。  

**主要特性**：  
- **双条件退出机制**：结合任务完成度指标和 Claude 返回的 `EXIT_SIGNAL` 判断是否终止循环。  
- **全面测试覆盖**：包含 164 个单元测试和 144 个集成测试，确保功能稳定性。  
- **依赖管理**：自动检测并提示缺失的依赖（如 Claude Code CLI、tmux）。  
- **日志与会话管理**：支持日志查看、会话分离/重新连接（tmux 控制）。