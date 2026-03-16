### [LockGit gochat](https://github.com/LockGit/gochat)  ![GitHub Repo stars](https://img.shields.io/github/stars/LockGit/gochat?style=social)

gochat 是一个基于纯 Go 实现的轻量级即时通讯（IM）系统。支持私信与房间广播功能，采用分层架构并通过 RPC 进行层间通讯，支持水平扩展。接入层兼容 WebSocket 和 TCP 协议，服务发现基于 etcd，消息存储与投递使用 Redis（支持替换为 Kafka/RabbitMQ）。提供 Docker 一键部署方案，支持跨平台编译，并配套有 TypeScript + React 前端界面。