
---
title: centrifugo
---

### [centrifugal centrifugo](https://github.com/centrifugal/centrifugo)

Centrifugo 是一个开源的可扩展实时消息服务器，支持 WebSocket、HTTP 流、Server-Sent Events（SSE）、GRPC 和 WebTransport 等多种传输协议，通过频道订阅实现发布/订阅（PUB/SUB）功能，适用于构建聊天应用、实时评论、多人游戏、协作工具等场景。它提供官方 SDK 支持浏览器和移动端开发，同时兼容无 SDK 的单向通信场景。主要特性包括：基于 Redis 或 Nats 的可扩展架构、HTTP/GRPC 接口供后端交互、异步 PostgreSQL/Kafka 消费者支持事务性出站和 CDC 模式、灵活的认证机制（JWT 和代理验证）、频道权限控制与命名空间管理、消息历史恢复与压缩（Fossil 算法）、在线用户 Presence 状态追踪、支持 RPC 调用、JSON 与 Protobuf 数据传输、内置 Admin 管理界面、Prometheus 监控指标及 Grafana 仪表盘。用户可通过官方文档获取安装、教程和设计指南，社区支持通过 Telegram、Discord 和 Twitter 参与。