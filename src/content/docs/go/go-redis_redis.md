
---
title: go-redis
---

### [redis go-redis](https://github.com/redis/go-redis)  ![GitHub Repo stars](https://img.shields.io/github/stars/redis/go-redis?style=social)

go-redis 是 Go 语言的官方 Redis 客户端库，功能总结如下：

1. **核心支持**：支持 Redis 7.0+ 版本（当前主要支持 8.x 系列），提供除 QUIT 和 SYNC 外的所有 Redis 命令及自动连接池管理。
2. **架构兼容**：支持 Redis Cluster 集群、Sentinel 高可用、Pub/Sub 发布订阅及 Redis 哨兵模式。
3. **高级特性**：支持管道（Pipelines）和事务、Lua 脚本、Redis 概率数据结构及 OpenTelemetry 性能监控。
4. **认证与协议**：兼容 RESP2 和 RESP3 协议，提供流式凭证、上下文绑定及静态凭证等多种认证方式，支持 Entra ID 集成。
5. **灵活配置**：支持自定义读写缓冲区大小、Typed Errors 错误类型处理及 Hooks 扩展机制。