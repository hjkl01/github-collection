
---
title: citus
---

### [citusdata citus](https://github.com/citusdata/citus)  ![GitHub Repo stars](https://img.shields.io/github/stars/citusdata/citus?style=social)

Citus 是一个 100% 开源的 PostgreSQL 扩展，旨在将 PostgreSQL 转换为分布式数据库，以实现任意规模下的高性能。

**核心功能：**
1. **分布式表**：在节点集群中分片存储，整合 CPU、内存、存储和 I/O 资源。
2. **引用表**：在所有节点复制，优化连接和查询性能。
3. **分布式查询引擎**：跨集群并行路由和执行 SELECT、DML 等操作。
4. **列式存储**：自动压缩数据，加速扫描。
5. **Schema 分片**：支持多租户应用按 Schema 分片（12.0+）。

**应用场景：**
适用于高事务吞吐量、多租户 SaaS 应用、实时分析、时间序列及 IoT 数据处理。

**部署与兼容性：**
保留 PostgreSQL 的全部功能特性（如 PostGIS、JSONB），支持高可用架构（如 Patroni），并提供本地安装、Docker 及 Azure 托管等多种部署方案。