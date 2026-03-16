### [tair-opensource RedisShake](https://github.com/tair-opensource/RedisShake)  ![GitHub Repo stars](https://img.shields.io/github/stars/tair-opensource/RedisShake?style=social)

RedisShake 是一款用于 Redis 数据转换与迁移的开源工具。

**核心特性：**
1. **零停机迁移**：支持无缝数据传输，确保服务不中断且无数据丢失。
2. **广泛兼容**：支持 Redis（2.8-8.4.x）和 Valkey（8.x-9.x），涵盖单机、主从、哨兵、集群及阿里云 Tair、AWS 等云数据库，兼容 Tair 扩展模块。
3. **灵活处理**：支持 PSync、RDB、Scan 数据读取方式，提供脚本化数据转换和过滤规则配置。
4. **便捷部署**：支持直接下载、Docker 运行及源码构建，通过 TOML 配置文件管理。

**限制说明：**
v4 版本不支持断点续传（重启后需全量重同步），假设集群拓扑静态不变（不支持拓扑变更），适用于一次性数据迁移场景，不建议用于长周期持续同步。