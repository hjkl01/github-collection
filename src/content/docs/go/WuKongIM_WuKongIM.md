
---
title: WuKongIM
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/WuKongIM/WuKongIM?style=social) ](https://github.com/WuKongIM/WuKongIM)
### [WuKongIM WuKongIM](https://github.com/WuKongIM/WuKongIM)

**项目核心内容总结：**

悟空IM是一款基于Go语言开发的高性能通用通讯服务，支持即时通讯、消息中台、物联网、音视频信令、直播弹幕等场景，具备去中心化设计、故障自动转移、集群自动扩容等特性，采用自研二进制协议和分布式数据库，实现高并发、低延迟的消息传输。项目不依赖任何中间件，提供Websocket、TLS 1.3等协议支持，消息可永久存储且支持多设备同步。

**使用方法：**
- 快速部署可通过Docker命令一键启动（`docker compose up -d`）；
- 源码开发支持单机模式（`go run main.go`）和分布式模式（多节点配置启动）；
- 客户端提供JavaScript、Android、iOS等多平台SDK，支持消息发送、接收、频道订阅等功能。

**主要特性：**
1. **高可用性**：基于魔改Raft协议实现故障自动转移，支持集群节点故障时无缝切换。
2. **高性能**：自研分布式数据库和二进制协议，单节点支持高并发，低资源消耗。
3. **多场景支持**：涵盖即时通讯、消息中台、物联网、直播弹幕等，支持消息漫游、多设备同步。
4. **易用性**：提供多语言SDK和完整部署文档，支持Web、移动端等多端接入。
5. **去中心化**：无需中心服务器，节点间直接通信，提升系统容灾能力。

**部署与扩展：**
- 提供Docker镜像和正式部署文档；
- 支持与第三方系统集成，配套SDK覆盖主流开发平台。