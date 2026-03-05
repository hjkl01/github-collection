
---
title: gochat
---

### [LockGit gochat](https://github.com/LockGit/gochat)  ![GitHub Repo stars](https://img.shields.io/github/stars/LockGit/gochat?style=social)

gochat 是一个使用纯 Go 语言实现的轻量级即时通讯（IM）系统。

1. **核心功能**：支持私信消息与房间广播消息，各层间通过 RPC 通讯，支持水平扩展。
2. **接入协议**：同时支持 WebSocket 和 TCP 接入，并实现两种协议的消息互通。
3. **架构设计**：包含 API、Connect（长连接）、Logic（业务逻辑）、Task（消息消费）及 Site 层，基于 etcd 实现服务发现。
4. **数据存储**：使用 Redis 作为消息队列与缓存载体（可替换为 Kafka/RabbitMQ），数据库默认使用 SQLite 但可替换为其他关系型数据库。
5. **部署与扩展**：支持 Docker 一键构建环境，利用 Go 交叉编译特性支持多平台快速运行。
6. **前端界面**：配套提供基于 TypeScript + React 的简易聊天室 UI。