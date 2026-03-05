
---
title: ydb
---

### [ydb-platform ydb](https://github.com/ydb-platform/ydb)  ![GitHub Repo stars](https://img.shields.io/github/stars/ydb-platform/ydb?style=social)

YDB 是一款开源分布式 SQL 数据库，兼具高可用性、可扩展性、严格一致性和 ACID 事务特性。其核心功能总结如下：

*   **混合存储模型**：支持行式和列式表以应对交易和分析负载，同时提供持久队列（Topics）用于数据传输。
*   **高容错与自动恢复**：可容忍磁盘、节点、机柜甚至数据中心故障，具备自动灾难恢复能力，确保数据冗余自动修复。
*   **弹性架构**：存储和计算层解耦，支持独立横向扩展；提供多租户和无服务器部署模式。
*   **广泛兼容**：使用 YQL SQL 语言，兼容 PostgreSQL 和 Kafka 接口；支持通过 Ansible、Kubernetes 或手动部署。
*   **大规模性能**：生产环境支持万级节点、PB 级数据存储及每秒数百万次分布式事务处理。