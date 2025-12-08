
---
title: nakama
---

### [heroiclabs nakama](https://github.com/heroiclabs/nakama)

**项目核心内容总结：**

Nakama 是一个用于开发多人在线游戏和应用的后端服务器，具备用户认证、实时通信、存储管理、多人匹配、模块化扩展等功能。其主要特性包括支持多种协议（如 REST、gRPC、WebSocket、rUDP），提供 Web 控制台用于管理玩家数据、查看服务指标、调试 API 等，还支持通过 Docker 快速部署，或使用预编译的二进制文件进行安装。Nakama 可以与 CockroachDB 数据库配合使用，以实现高可用性和分布式存储。

**使用方法：**

- **Docker 部署：** 通过 docker-compose 文件启动 Nakama 和数据库容器。
- **二进制文件部署：** 下载 Nakama 服务器和 CockroachDB 数据库，运行数据库并执行迁移脚本，最后启动 Nakama 服务。
- **客户端使用：** 支持多种语言的官方客户端库，如 C#、JavaScript、Java、Unreal、Godot 等，可通过 REST API 或 WebSocket 进行用户认证、数据交互等操作。

**主要特性：**

- 多协议支持（REST、gRPC、WebSocket、rUDP）；
- 实时通信与多人匹配；
- 数据存储与管理；
- Web 控制台用于监控和管理；
- 支持 Docker 和二进制部署；
- 提供模块化扩展能力；
- 与 CockroachDB 集成，支持高可用性与分布式架构。