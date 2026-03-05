
---
title: marmot
---

### [maxpert marmot](https://github.com/maxpert/marmot)  ![GitHub Repo stars](https://img.shields.io/github/stars/maxpert/marmot?style=social)

Marmot v2 是一款基于 Gossip 协议的无主分布式 SQLite 复制系统，支持分布式事务与最终一致性。

**核心功能：**
*   **无主架构**：无单点故障，任意节点均可接受写入，无需主节点选举，自动处理网络分区与故障恢复。
*   **MySQL 协议兼容**：支持标准 MySQL 客户端连接（如 DBeaver、CLI），兼容现有 ORM 与工具，支持运行分布式 WordPress。
*   **高级复制机制**：支持多数据库管理、DDL 语句自动幂等复制（带集群锁）、批量数据加载（`LOAD DATA`）及行级 CDC 变更捕获（兼容 Debezium 格式）。
*   **边缘优化**：客户端可直接读取本地 SQLite 文件以获得低延迟读取，支持读写分离与边缘侧车部署。
*   **一致性调优**：支持可调的一致性级别（ONE/QUORUM/ALL），冲突采用最后写入胜利（LWW）机制解决。
*   **扩展与集成**：支持加载 SQLite 扩展（如向量搜索），可发布 CDC 事件至 Kafka 或 NATS 等外部系统。

**适用场景：**
分布式 WordPress 部署、Lambda/边缘侧车场景、区域配置服务器、Geo 分布式目录数据等读密集型边缘计算场景。