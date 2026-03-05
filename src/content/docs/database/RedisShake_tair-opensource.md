
---
title: RedisShake
---

### [tair-opensource RedisShake](https://github.com/tair-opensource/RedisShake)  ![GitHub Repo stars](https://img.shields.io/github/stars/tair-opensource/RedisShake?style=social)

RedisShake 是由阿里云 Tair 团队维护的 Redis 数据转换与迁移工具。核心功能如下：

1. **迁移支持**：支持 Redis (2.8-8.4.x) 和 Valkey (8.x-9.x)，兼容单机、主从、哨兵及集群部署，实现零停机时间迁移。
2. **云服务集成**：无缝对接阿里云 Tair、AWS ElastiCache 和 MemoryDB。
3. **数据获取与处理**：支持 PSync、RDB、Scan 方式获取数据，提供脚本定制转换及键前缀过滤功能。
4. **模块兼容**：兼容 TairString、TairZSet 和 TairHash 模块。
5. **限制说明**：不支持断点续传及集群拓扑变更，适用于一次性数据迁移场景。