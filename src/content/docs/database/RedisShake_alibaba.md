
---
title: RedisShake
---

### [alibaba RedisShake](https://github.com/alibaba/RedisShake)  ![GitHub Repo stars](https://img.shields.io/github/stars/alibaba/RedisShake?style=social)

RedisShake 是一款用于 Redis 数据转换与迁移的工具。核心功能如下：
1. 支持零停机无缝迁移，兼容 Redis（2.8-8.4.x）及 Valkey（8.x-9.x），覆盖单机、主从、哨兵和集群部署模式。
2. 无缝集成阿里云 Tair、AWS ElastiCache 及 MemoryDB 等主流云数据库服务。
3. 支持 TairString、TairZSet、TairHash 等扩展模块。
4. 提供 PSync、RDB、Scan 多种数据读取方式，支持自定义脚本数据转换和过滤规则。
5. 适用于一次性数据迁移场景，不支持断点续传及集群拓扑动态变化感知。