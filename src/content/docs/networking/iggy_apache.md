
---
title: iggy
---

### [apache iggy](https://github.com/apache/iggy)  ![GitHub Repo stars](https://img.shields.io/github/stars/apache/iggy?style=social)

Apache Iggy 是一款基于 Rust 开发的高性能持久化消息流平台，采用线程对核心无共享架构与 io_uring 技术，原生支持 QUIC、WebSocket、TCP 和 HTTP 协议，具备每秒百万级消息的超低延迟吞吐能力。

核心功能包括：
1. **存储与流处理**：支持流、主题、分区及消费者组，提供消息过期、自动偏移量提交、去重及多种拉取策略。
2. **安全性**：支持 TLS 传输加密、AES-256-GCM 数据加密、用户认证授权及细粒度权限控制。
3. **开发运维**：提供多语言 SDK（Rust/Java/Python 等）、CLI、Web UI 及 RESTful API，支持单二进制部署。
4. **扩展性**：支持自定义 Rust 连接器插件、MCP 协议对接 LLM、OpenTelemetry 监控及 S3 数据备份。
5. **架构**：当前为单节点部署，未来计划支持基于 VSR 的集群复制。