
---
title: RedisShake
---

### [alibaba RedisShake](https://github.com/alibaba/RedisShake)

**RedisShake 核心内容总结：**

**项目功能**  
RedisShake 是一款支持 Redis 数据迁移与转换的工具，核心功能包括：  
1. **零停机迁移**：迁移过程中无数据丢失或服务中断。  
2. **兼容性**：支持 Redis（≤7.4）和 Valkey（≤7.2），适配单机、主从、哨兵、集群等部署方式。  
3. **云服务集成**：兼容阿里云 Tair、AWS ElastiCache 和 MemoryDB 等云数据库。  
4. **模块支持**：兼容 TairString、TairZSet、TairHash 等扩展模块。  
5. **数据处理**：支持通过脚本自定义数据转换规则，或通过过滤规则筛选数据。  

**使用方法**  
1. **下载**：从 [Releases](https://github.com/tair-opensource/RedisShake/releases) 获取二进制文件。  
2. **Docker**：运行容器并配置源和目标地址。  
3. **自行构建**：克隆代码后执行 `build.sh` 构建。  
4. **配置文件**：通过 `shake.toml` 定义源地址、目标地址及过滤规则，例如跳过特定前缀的键。  

**主要特性**  
- **跨版本迁移**：迁移前建议使用 [resp-compatibility](https://github.com/tair-opensource/resp-compatibility) 工具检查兼容性。  
- **版本演进**：从 2.x（稳定性提升）到 4.x（增强读取器、配置、可观测性）。  
- **开源许可**：采用 MIT 协议开源。  

**其他**  
- 支持通过 PSync、RDB、Scan 等方式获取数据。  
- 提供中文和英文双语文档（[中文](https://tair-opensource.github.io/RedisShake/) / [English](https://tair-opensource.github.io/RedisShake/en/)）。