
---
title: apscheduler
---

### [agronholm apscheduler](https://github.com/agronholm/apscheduler)  ![GitHub Repo stars](https://img.shields.io/github/stars/agronholm/apscheduler?style=social)

APScheduler 是一个适用于 Python 的任务调度与任务队列系统，支持同步及异步（asyncio/Trio）模式，可集成于 WSGI 或 ASGI 兼容的 Web 应用。系统提供 Cron 风格、基于间隔、基于日历及一次性调度等内置触发器，支持自定义触发器及组合逻辑。支持 PostgreSQL、MySQL、SQLite 和 MongoDB 持久化存储，确保任务数据在多节点共享及进程重启后存活，并通过 PostgreSQL、Redis、MQTT 事件代理实现高可用与水平扩展。其他功能包括限制最大并发任务数、任务启动延迟限制及抖动。注意：v4.0 系列目前为预发布版，存在向后不兼容风险，不建议在生产环境使用。