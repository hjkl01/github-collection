
---
title: walrus
---

### [nubskr walrus](https://github.com/nubskr/walrus)  ![GitHub Repo stars](https://img.shields.io/github/stars/nubskr/walrus?style=social)

Walrus 是一个基于高性能日志存储引擎构建的分布式消息流平台，提供容错流传输与自动负载均衡。

核心功能：
1. **分布式架构**：支持 3+ 节点集群，使用 Raft 共识管理元数据，实现自动领导权轮换与故障恢复。
2. **分段管理**：基于段（Segment）分区，领导权随段轮换自动分布负载，支持密封段历史读取。
3. **高性能存储**：Linux 下利用 io_uring 优化，写入性能对标 Kafka；核心引擎可作为独立 Rust 库使用。
4. **强一致性**：采用基于租约的写围栏机制，确保单段单写；通过 TLA+ 形式化规格验证数据正确性。
5. **简单易用**：提供简单的 TCP 文本客户端协议及交互式 CLI，客户端可连接任意节点自动路由。