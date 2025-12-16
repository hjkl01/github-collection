
---
title: citus
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/citusdata/citus?style=social) ](https://github.com/citusdata/citus)
### [citusdata citus](https://github.com/citusdata/citus)

**Citus 核心内容总结：**  
Citus 是基于 PostgreSQL 的分布式数据库扩展，支持水平扩展数据仓库和 OLTP（在线事务处理）工作负载，适用于大规模数据分析和高并发事务场景。  

**主要功能与特性：**  
1. **分布式查询引擎**：支持并行查询、跨节点数据分析，兼容 PostgreSQL 的 JSONB、数组、HyperLogLog 等数据类型及扩展。  
2. **列式存储**：通过压缩旧数据分区优化存储效率，提升查询性能。  
3. **多租户支持**：通过租户 ID 分片和数据共定位，实现复杂租户级查询与事务的水平扩展。  
4. **时间序列优化**：集成 PostgreSQL 分区功能，支持高效时间序列数据写入与分析。  
5. **微服务架构适配**：提供基于 schema 的分片，支持微服务独立管理数据存储。  
6. **地理空间支持**：兼容 PostGIS 扩展，适用于大规模地理信息应用。  

**使用方法：**  
- 安装 Citus 扩展并配置集群节点；  
- 定义分片表（按租户或业务逻辑）与参考表（集中存储共享数据）；  
- 使用列式存储压缩历史数据；  
- 通过 PostgreSQL 客户端进行查询、监控及管理。  

**适用场景：**  
实时分析仪表盘、时间序列数据处理、多租户 SaaS 应用、微服务数据分片、地理空间数据扩展等。