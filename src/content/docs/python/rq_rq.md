
---
title: rq
---

### [rq rq](https://github.com/rq/rq)  ![GitHub Repo stars](https://img.shields.io/github/stars/rq/rq?style=social)

RQ（Redis Queue）是一个基于 Redis 或 Valkey 的轻量级 Python 后台任务队列库。它设计简洁，易于集成到 Web 栈中，适用于从简单应用到企业级系统的各种规模项目。

核心功能包括：
1. **异步任务处理**：将耗时函数入队，由 Worker 在后台执行。
2. **任务优先级**：支持将任务插入队列前端，或使用多队列机制区分优先级。
3. **任务调度**：支持指定绝对时间执行、相对时间延迟执行，以及基于 Cron 语法和固定间隔的周期性任务调度。
4. **失败重试**：支持配置失败任务的重试次数及间隔。
5. **重复任务**：支持任务按指定次数和间隔重复执行。
6. **多种 Worker 模式**：提供 SimpleWorker、Worker、SpawnWorker 及多进程池，平衡性能与隔离性。

项目依赖 Redis >= 5 或 Valkey >= 7.2，安装方式为 `pip install rq`。