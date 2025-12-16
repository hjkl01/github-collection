
---
title: celery
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/celery/celery?style=social) ](https://github.com/celery/celery)
### [celery celery](https://github.com/celery/celery)

**Celery核心内容总结：**

1. **项目功能**  
   Celery是一个基于Python的分布式任务队列系统，用于处理异步任务和定时任务。支持多种消息中间件（如RabbitMQ、Redis、Amazon SQS等）和结果存储后端（如数据库、云存储、文件系统等），适用于需要解耦和异步处理的场景。

2. **使用方法**  
   - 安装：可通过`pip`安装，或从源码编译。  
   - 配置：定义任务函数，通过`@app.task`装饰器标记。  
   - 启动：使用`celery worker`启动工作进程，通过消息中间件接收任务并执行。  
   - 扩展：支持多种并发方式（如Eventlet、Gevent）和插件机制。

3. **主要特性**  
   - **多中间件支持**：兼容AMQP、Redis、SQS、RabbitMQ等消息传输协议。  
   - **灵活后端**：结果可存储在数据库（如SQLAlchemy、MongoDB）、云存储（如S3、Azure）或本地文件系统。  
   - **任务管理**：支持任务重试、优先级、定时任务（使用Cron表达式）、任务链式调用。  
   - **监控与调试**：提供管理界面（如Flower）用于实时监控任务状态和性能。  
   - **高可用性**：支持集群部署、负载均衡和故障转移。  

4. **适用场景**  
   适用于需要处理大量异步任务、需要延迟执行或周期性任务的系统，如Web应用后台处理、数据处理流水线、实时消息队列等。  

5. **社区与支持**  
   拥有活跃的社区，提供详细的文档和问题跟踪系统，支持通过GitHub提交贡献。