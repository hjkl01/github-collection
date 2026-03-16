### [git-ai-project git-ai](https://github.com/git-ai-project/git-ai)  ![GitHub Repo stars](https://img.shields.io/github/stars/git-ai-project/git-ai?style=social)

git-ai 是一个开源的 Git 扩展工具，旨在追踪和记录仓库中 AI 生成的代码。其核心功能包括：

1.  **自动归属追踪**：安装后自动将每行 AI 编写的代码与生成它的代理、模型及对话记录关联，保存代码背后的意图和架构决策。
2.  **智能 blame 替代**：`git-ai blame` 命令可替代 `git blame`，清晰显示每一行代码背后的 AI 模型、会话 ID 及作者信息。
3.  **广泛兼容**：支持 GitHub Copilot、Cursor、Claude Code、Windsurf 等多种主流 AI 编程助手。
4.  **无感集成**：无需针对每个仓库单独配置，基于 Git Notes 标准存储元数据，不污染 Git 历史，支持完全离线使用。
5.  **上下文增强**：提供 `/ask` 技能，使 AI 助手能够查询原始提示词和会话记录，理解代码生成的“为什么”，从而生成更高质量的代码。
6.  **数据分析与可观测性**：提供统计命令追踪 AI 代码采纳率、接受率及生命周期指标，企业版支持团队级的 AI 代码仪表盘和 PR 级监控。
7.  **IDE 插件支持**：提供 VS Code、Cursor 等编辑器的插件，在行号侧边栏实时显示 AI 代码归属标记及提示信息。