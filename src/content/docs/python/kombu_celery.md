
---
title: kombu
---

### [celery kombu](https://github.com/celery/kombu)  ![GitHub Repo stars](https://img.shields.io/github/stars/celery/kombu?style=social)

Kombu 是 Python 消息库，通过提供 AMQP 协议的高层接口简化消息传递。它支持可插拔的传输方式，兼容多种消息服务器（如 RabbitMQ、Redis、Amazon SQS、MongoDB 等）。核心功能包括消息负载的自动编码、序列化与压缩，跨传输的一致性异常处理，以及优雅的连接错误恢复。项目提供生产者、交换器、队列和消费者等标准消息组件，支持直接、主题和广播等多种路由模式，并内置内存传输以方便单元测试。