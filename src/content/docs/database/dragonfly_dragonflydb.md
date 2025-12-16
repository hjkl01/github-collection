
---
title: dragonfly
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/dragonflydb/dragonfly?style=social) ](https://github.com/dragonflydb/dragonfly)
### [dragonflydb dragonfly](https://github.com/dragonflydb/dragonfly)

**项目核心内容总结：**  
Dragonfly 是一个高性能、低延迟的内存数据库，支持 Redis（约185个命令）和 Memcached 协议（除 `cas` 命令外）。其核心特性包括：  
1. **架构设计**：基于共享无架构（shared-nothing）和 VLL 事务框架，实现多线程并发处理，支持原子性操作；采用 Dash 哈希表设计，提升 CPU 和内存效率。  
2. **缓存优化**：内置自适应缓存算法，支持 `--cache_mode` 开启，按访问概率淘汰数据；提供零内存开销的高效缓存命中率。  
3. **功能特性**：支持 Redis 5.0 级别 API、Memcached 协议、HTTP 控制台、Prometheus 指标监控；具备快照备份（`snapshot_cron`）、分布式日志复制（未来支持）等功能。  
4. **使用方法**：通过命令行参数配置（如 `--requirepass` 设置密码、`--maxmemory` 限制内存、`--cache_mode` 启用缓存），支持 Docker 部署；提供 TLS、日志管理等高级选项。  

**主要优势**：兼顾高吞吐量与亚毫秒级延迟，适用于云原生场景，兼容 Redis/Memcached 接口，开箱即用。