
---
title: asynq
---

### [hibiken asynq](https://github.com/hibiken/asynq)  ![GitHub Repo stars](https://img.shields.io/github/stars/hibiken/asynq?style=social)

Asynq 是一个基于 Redis 的 Go 语言分布式任务队列库，用于异步任务的调度与处理，支持高可用与水平扩展。

核心功能包括：
- **可靠性**：保证任务至少执行一次，支持失败自动重试及 Worker 崩溃恢复。
- **调度与管理**：支持任务延迟与周期执行、去重、超时控制、任务聚合及暂停队列。
- **队列策略**：提供加权与严格优先级队列。
- **监控与运维**：集成 Prometheus 指标监控，支持 Redis Sentinel 高可用，提供 Web UI 和 CLI 工具。
- **扩展性**：灵活的 Handler 接口，支持中间件注入。