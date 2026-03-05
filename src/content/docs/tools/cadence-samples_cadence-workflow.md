
---
title: cadence-samples
---

### [cadence-workflow cadence-samples](https://github.com/cadence-workflow/cadence-samples)  ![GitHub Repo stars](https://img.shields.io/github/stars/cadence-workflow/cadence-samples?style=social)

该项目是 Cadence 工作流编排引擎的示例代码集合，旨在通过实用案例展示 Cadence 构建可靠、可扩展应用的能力。Cadence 是一个分布式、持久且高可用的编排引擎。

项目主要包含三类示例：
1. **基础示例**：包括 Hello World、问候语、Cron 定时、定时器、延迟启动、并行分支、拆分合并及优先选择模式。
2. **高级示例**：涵盖条件分支、重试、取消、互斥锁、查询、子工作流、动态执行、本地活动、版本控制、搜索属性、上下文传播、分布式追踪、副作用、批量处理及故障恢复。
3. **业务应用示例**：涉及费用审批、分布式文件处理、领域特定语言（DSL）及粒子群优化（PSO）。

项目提供基于 Docker 的快速环境搭建（含服务端与 Web UI），支持使用 Go 语言构建、测试及运行。示例支持多种运行模式（如 worker、trigger、query、signal），帮助开发者学习 Cadence 核心概念并落地实际工作流场景。