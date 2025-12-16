
---
title: apscheduler
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/agronholm/apscheduler?style=social) ](https://github.com/agronholm/apscheduler)
### [agronholm apscheduler](https://github.com/agronholm/apscheduler)

**核心内容总结：**

APScheduler 是一个 Python 任务调度器和任务队列系统，支持同步和异步（兼容 asyncio/Trio）应用，适用于单进程及大规模分布式部署。主要功能包括：  
- **调度方式**：支持 Cron 风格、间隔、日历周期、单次触发等调度机制，支持多种触发器组合。  
- **持久化存储**：提供 PostgreSQL、MySQL、SQLite、MongoDB 等数据存储后端，支持多实例共享和故障恢复。  
- **分布式支持**：通过 PostgreSQL、Redis、MQTT 等事件代理实现多调度器/工作者协同。  
- **特性**：支持限制任务并发数、延迟启动时间、随机延迟（Jitter）等；可自定义调度逻辑。  

**使用方法**：  
- 提供 WSGI/ASGI 集成示例，支持 Web 应用嵌入。  
- 文档、源码及问题反馈渠道可通过官网链接获取。  

**注意事项**：  
当前 4.0 版本为预发布版，可能包含不兼容变更，不适合生产环境使用。