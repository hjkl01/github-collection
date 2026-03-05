
---
title: git-ai
---

### [git-ai-project git-ai](https://github.com/git-ai-project/git-ai)  ![GitHub Repo stars](https://img.shields.io/github/stars/git-ai-project/git-ai?style=social)

Git AI 是一个开源 Git 扩展，用于追踪和标注仓库中的 AI 生成代码。

1. **核心功能**：自动将 AI 编写的每一行代码关联到对应的智能体、模型及对话记录，保留代码意图与决策上下文。
2. **命令行工具**：`git commit` 统计 AI 代码比例，`git-ai blame` 替代标准 `git blame` 逐行显示人类或 AI 作者。
3. **广泛兼容**：支持 Cursor、Copilot、Claude Code 等多种 AI 助手，无需修改工作流程即可自动追踪。
4. **隐私安全**：基于 Git Notes 标准存储归属信息，对话记录可选择本地、云端或自托管，确保仓库轻量且不含敏感信息。
5. **增强分析**：提供 `/ask` 技能增强 Agent 理解能力，IDE 插件可视化展示归属，支持团队级的 AI 代码统计与全生命周期追踪。

项目遵循 Apache 2.0 协议，在重基、合并等操作中自动维护归属信息的完整性。