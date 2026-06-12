### [agent-skills](https://github.com/addyosmani/agent-skills) ![GitHub Repo stars](https://img.shields.io/github/stars/addyosmani/agent-skills?style=social)

这是一个为 AI 编码代理提供“生产级工程技能”的项目，通过可执行的技能工作流，强制代理按资深工程师标准完成完整研发流程：定义需求、制定计划、增量开发、测试验证、代码评审与上线发布。项目提供 7 个斜杠命令（`/spec`、`/plan`、`/build`、`/test`、`/review`、`/code-simplify`、`/ship`）作为生命周期入口，并内置 22 个技能（21 个工程技能 + 1 个元技能），覆盖需求澄清、任务拆解、TDD、API/UI 设计、调试、质量审查、安全加固、性能优化、Git 工作流、CI/CD、迁移下线、文档与发布等关键环节。

每个技能都采用统一结构（触发条件、步骤流程、反借口机制、风险信号、验证证据），强调“先流程后代码”“验证不可妥协”“以证据证明可用”，避免代理跳过规格、测试和安全检查。项目还提供 3 类专家代理人格（代码评审、测试、安全审计）、4 份快速检查清单，以及对 Claude Code、Cursor、Gemini CLI、Windsurf、OpenCode、GitHub Copilot、Kiro 等工具的集成支持，目标是让 AI 产出从原型质量提升到可上线的工程质量。