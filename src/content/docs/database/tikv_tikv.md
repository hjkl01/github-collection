
---
title: tikv
---

### [tikv tikv](https://github.com/tikv/tikv)

**项目简介**  
TiKV 是一个基于 Rust 的分布式、支持事务的键值数据库，由 PingCAP 开发，用于与 TiDB 配合，提供高可扩展性、外部一致性事务及混合负载能力。其设计借鉴了 Google 的 Spanner、BigTable 等系统及 Raft 共识算法。

**主要特性**  
- **Geo-Replication**：通过 Raft 和 Placement Driver（PD）实现跨地域复制。  
- **水平扩展**：支持自动分片和数据迁移，可扩展至 PB 级数据。  
- **分布式事务**：提供外部一致性事务（类似 Google Spanner），支持快照隔离和锁机制。  
- **Coprocessor 框架**：支持分布式计算（类似 HBase）。  
- **与 TiDB 协同**：与 TiDB 集成，形成 HTAP 数据库解决方案。

**使用方法**  
1. **快速部署**：  
   - 使用 TiUP 工具一键部署测试环境。  
   - 通过二进制文件手动启动 PD 和 TiKV 实例。  
   - 使用 Docker Compose 部署完整集群（3 PD + 3 TiKV 节点）。  
2. **客户端支持**：提供 Go、Java、Rust、C 等语言的客户端驱动。  
3. **源码构建**：参考 CONTRIBUTING.md 文档进行编译。

**其他信息**  
- **许可证**：Apache 2.0。  
- **安全审计**：由 Cure53 进行第三方安全审计。  
- **社区**：通过 Slack、GitHub、Stack Overflow 等渠道参与交流。