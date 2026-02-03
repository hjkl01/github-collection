
---
title: marmot
---

### [maxpert marmot](https://github.com/maxpert/marmot)  ![GitHub Repo stars](https://img.shields.io/github/stars/maxpert/marmot?style=social)

**项目核心内容总结：**  
Marmot 是一个基于 SQLite 的分布式数据库系统，兼容 MySQL 协议，支持高可用、强一致性、自动复制和跨节点数据同步。主要功能包括：  
1. **核心特性**：  
   - 自动 ID 生成（支持 53 位或 64 位模式）；  
   - 实时变更数据捕获（CDC），可将数据变更同步到 Kafka/NATS；  
   - 支持 SQLite 扩展（如向量计算）；  
   - 内置 Prometheus 监控指标，支持日志管理与文件轮转；  
   - 通过 MySQL 协议提供服务，支持 Unix 套接字连接。  

2. **使用方法**：  
   - 通过 `config.toml` 配置数据库参数（如监听地址、线程数、备份策略）；  
   - 启用 CDC 功能需配置 Kafka/NATS 的连接信息与数据过滤规则；  
   - 备份方案推荐 Litestream（兼容 SQLite WAL 模式），或通过 CDC 流入外部存储。  

3. **性能表现**：  
   - 本地 3 节点测试中，单节点写入吞吐量达 4,175 ops/sec，混合负载下 P99 延迟约 85ms；  
   - 支持跨区域部署，但需根据网络延迟调整预期性能（如 QUORUM 写入 P99 延迟可能达 50-200ms）。  

4. **适用场景**：  
   - 适合需要 MySQL 兼容性、分布式高可用及轻量级数据库的场景，如微服务数据同步、实时分析等。