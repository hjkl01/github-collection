
---
title: RedisShake
---

### [alibaba RedisShake](https://github.com/alibaba/RedisShake)  ![GitHub Repo stars](https://img.shields.io/github/stars/alibaba/RedisShake?style=social)

RedisShake 是一款 Redis 数据转换与迁移工具，主要功能包括：

1. **零停机迁移**：支持无缝数据迁移，确保服务不中断。
2. **广泛兼容性**：支持 Redis (2.8-8.4.x) 和 Valkey (8.x-9.x)，覆盖单机、主从、哨兵及集群模式；兼容阿里云 Tair、AWS 云服务及 Tair 模块。
3. **灵活数据获取与处理**：支持 PSync、RDB、Scan 读取方式，提供脚本转换和自定义数据过滤规则。
4. **便捷部署**：支持命令行、Docker 及源码构建。

注：不支持断点续传和集群拓扑变更感知，适用于一次性数据迁移场景。