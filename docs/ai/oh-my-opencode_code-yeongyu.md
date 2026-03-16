### [code-yeongyu oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode)  ![GitHub Repo stars](https://img.shields.io/github/stars/code-yeongyu/oh-my-opencode?style=social)

Oh My OpenCode 是基于 OpenCode 的多模型 AI 编程协作框架，通过编排不同大模型（如 Claude、GPT、Kimi 等）的优势避免单一锁定。

核心功能：
1. **一键工作流**：运行 `ultrawork` 命令自动激活所有代理，直至任务完成。
2. **多代理协作**：包含 Sisyphus（编排）、Hephaestus（执行）、Prometheus（规划）等专用代理并行作业。
3. **精准编辑工具**：采用哈希锚定技术防止上下文错误，结合 LSP 和 AST-Grep 实现 IDE 级重构。
4. **生态兼容**：完全兼容 Claude Code 的插件、Hook 和技能，内置搜索及文档 MCP 服务。
5. **智能辅助**：支持自动项目上下文生成、后台任务调度、代码注释检查及任务强制完成。