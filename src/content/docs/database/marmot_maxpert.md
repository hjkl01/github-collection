
---
title: marmot
---

### [maxpert marmot](https://github.com/maxpert/marmot)  ![GitHub Repo stars](https://img.shields.io/github/stars/maxpert/marmot?style=social)

Marmot v2 是一款基于 Gossip 协议的无主分布式 SQLite 复制系统，兼容 MySQL 协议，支持标准 MySQL 客户端（如 DBeaver、mysql CLI）直接连接。

主要功能特性：
- **无主架构**：无单点故障，任意节点均可接受写入，无需领导节点选举及故障转移协调。
- **分布式一致性**：支持 Percolator 风格事务与冲突检测，提供 ONE、QUORUM、ALL 可调节的一致性级别。
- **高兼容性**：完整支持 WordPress 所需 MySQL 函数、分布式 DDL 复制、批量数据加载（LOAD DATA）及多数据库管理。
- **CDC 能力**：支持行级变更数据捕获，可发布 Debezium 兼容格式事件至 Kafka 或 NATS 等消息系统。
- **边缘优化**：专为读密集边缘场景设计，支持本地 SQLite 直读、读写分离、自动故障转移、快照缓存及抗熵修复。
- **安全与运维**：支持预共享密钥（PSK）认证、事务日志自动 GC 协调、自动冲突合并及 Prometheus 监控。
- **ID 生成**：提供 JS 安全的 53 位自增 ID 模式，确保在 JavaScript 环境中无精度丢失。

适用于分布式 WordPress、边缘向量数据库、区域配置服务器及全球分布的产品目录等读密集型场景。