### [skills](https://github.com/mattpocock/skills) ![GitHub Repo stars](https://img.shields.io/github/stars/mattpocock/skills?style=social)

该项目是一个面向“真实工程开发”的 AI Agent 技能集合，用于帮助开发者在完整工程流程中高效工作，而不只是快速拼代码。功能按四类组织：

1. **规划与设计**  
- 将当前讨论直接整理为 PRD 并提交 GitHub Issue（to-prd）  
- 将计划/PRD 拆分为可独立领取的纵向切片任务（to-issues）  
- 通过持续追问完善方案与设计决策（grill-me）  
- 为模块生成多种差异化接口设计方案（design-an-interface）  
- 通过访谈生成可小步提交的重构计划并落地为 Issue（request-refactor-plan）

2. **开发实现**  
- 基于红绿重构循环执行 TDD 开发与修复（tdd）  
- 排查缺陷、定位根因并产出基于 TDD 的修复 Issue（triage-issue）  
- 结合 CONTEXT.md 与 ADR 提升代码库架构（improve-codebase-architecture）  
- 将测试中的 `as` 断言迁移到 `@total-typescript/shoehorn`（migrate-to-shoehorn）  
- 快速搭建练习项目目录（题目/答案/讲解）结构（scaffold-exercises）

3. **工具与工程化配置**  
- 配置 Husky pre-commit（含 lint-staged、Prettier、类型检查、测试）（setup-pre-commit）  
- 配置 Claude Code 的 Git 防护钩子，拦截危险命令（git-guardrails-claude-code）

4. **写作与知识管理**  
- 规范化创建新技能（write-a-skill）  
- 优化文章结构与表达质量（edit-article）  
- 从对话中提取 DDD 统一语言词汇表（ubiquitous-language）  
- 在 Obsidian 中检索、创建与管理知识笔记（obsidian-vault）

整体上，这是一个可通过 `npx skills@latest add ...` 安装的技能库，覆盖从需求、设计、开发、重构到写作与知识沉淀的端到端工程实践。