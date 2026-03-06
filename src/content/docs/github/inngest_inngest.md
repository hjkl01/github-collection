
---
title: inngest
---

### [inngest inngest](https://github.com/inngest/inngest)  ![GitHub Repo stars](https://img.shields.io/github/stars/inngest/inngest?style=social)

Inngest 是一个持久化函数平台，旨在替代队列、状态管理和调度，让开发者无需管理基础设施即可编写可靠的工作流和后台任务。

**核心功能：**

1.  **多语言 SDK**：支持 TypeScript/JavaScript、Python、Go、Kotlin/Java 开发。
2.  **本地开发环境**：提供 Dev Server 和 CLI，实现本地开发与生产环境一致。
3.  **灵活部署**：支持部署至自有基础设施，或同步至 Inngest 云平台/自托管服务器。
4.  **函数组件**：由触发器（事件、定时任务、Webhook）、流控制（并发、限流、优先级）和步骤（自动重试、状态持久化）组成。
5.  **高可靠架构**：包含事件 API、运行器、队列、执行器、状态存储及数据库，确保任务恢复和长期运行。
6.  **自托管支持**：支持自行部署 Inngest 服务器。