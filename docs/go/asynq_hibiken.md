### [hibiken asynq](https://github.com/hibiken/asynq)  ![GitHub Repo stars](https://img.shields.io/github/stars/hibiken/asynq?style=social)

Asynq 是一个基于 Redis 的 Go 语言分布式任务队列库，支持任务的异步排队与 Worker 并发处理。核心功能包括：保证任务至少执行一次、任务调度、失败重试、Worker 崩溃自动恢复、加权与严格优先级队列、任务去重、超时与截止时间控制、任务聚合、周期性任务及支持中间件的灵活处理接口。项目支持多机器横向扩展，兼容 Redis Sentinel 高可用架构。此外，集成 Prometheus 监控指标，并提供 Web UI 和命令行工具用于任务及队列的监控与管理。