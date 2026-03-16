### [agronholm apscheduler](https://github.com/agronholm/apscheduler)  ![GitHub Repo stars](https://img.shields.io/github/stars/agronholm/apscheduler?style=social)

APScheduler 是适用于 Python 的任务调度与任务队列系统，支持同步及异步（asyncio 或 Trio）应用，可集成 WSGI 或 ASGI 兼容的 Web 应用。支持持久化存储，可通过共享数据实现多节点部署、高可用及水平扩展。

核心特性：
- 存储后端：PostgreSQL、MySQL、SQLite、MongoDB
- 事件代理：PostgreSQL、Redis、MQTT
- 触发器：支持 Cron、间隔、日历、一次性调度，允许自定义及组合
- 任务控制：限制并发数、启动延迟及抖动（随机延迟）

注意：v4.0 系列为预发布版本，存在不向后兼容的变更，不建议在生产环境使用。