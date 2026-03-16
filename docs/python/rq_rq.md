### [rq rq](https://github.com/rq/rq)  ![GitHub Repo stars](https://img.shields.io/github/stars/rq/rq?style=social)

RQ（Redis Queue）是一个基于 Redis 或 Valkey 的 Python 库，用于在后台队列中处理和调度作业，适用于各种规模的项目。

主要功能：
1. **后台作业处理**：将长时间或阻塞函数加入队列，由 Worker 异步执行。
2. **优先级管理**：支持前端入队或多队列优先级排序。
3. **任务调度**：支持定时执行、延迟执行、固定间隔重复执行。
4. **容错机制**：支持配置失败作业的重试次数和间隔。
5. **周期性任务**：支持基于 Cron 语法或时间间隔的自动调度。
6. **Worker 运行**：提供多种 Worker 模式以平衡执行效率与沙箱隔离性，支持多进程集群。

需 Redis >= 5 或 Valkey >= 7.2。