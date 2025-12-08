
---
title: RedisJSON
---

### [RedisJSON RedisJSON](https://github.com/RedisJSON/RedisJSON)

**核心内容总结：**  
RedisJSON 是 Redis 的一个模块，将 JSON 作为原生数据类型集成到 Redis 中，支持存储、更新和查询 JSON 数据。其核心功能包括：  
1. **JSON 标准支持**：完全兼容 ECMA-404 JSON 标准，支持 JSONPath 语法进行数据检索。  
2. **高效存储**：以二进制树结构存储 JSON 文档，实现对子元素的快速访问。  
3. **原子操作**：提供针对所有 JSON 数据类型的原子级操作。  
4. **与 RediSearch 集成**：支持通过 RediSearch 实现二次索引，增强查询能力。  

**使用方法**：  
通过 Redis 命令操作 JSON 数据，例如使用 `JSON.SET` 存储、`JSON.GET` 获取、`JSON.QUERY` 结合 JSONPath 查询特定字段。  

**注意事项**：  
从 Redis 8 开始，JSON 功能已内置，无需单独安装 RedisJSON 模块。许可证支持 RSALv2、SSPLv1 或 AGPLv3（具体以 Redis 官方仓库为准）。