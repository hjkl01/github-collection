### [brainix pottery](https://github.com/brainix/pottery)  ![GitHub Repo stars](https://img.shields.io/github/stars/brainix/pottery?style=social)

Pottery 是一个 Python 库，旨在提供更直观的 Redis 访问方式并实现微服务弹性模式。核心功能包括：

1. **Redis 数据结构**：提供与 Python 原生 dict、set、list、deque、Counter 兼容的 Redis 后端容器（如 RedisDict），键值需为 JSON 可序列化。
2. **分布式同步**：实现分布式锁（Redlock、AIORedlock）和同步装饰器（synchronize），用于协调线程、进程及跨机器资源访问；提供 RedisSimpleQueue 实现跨机器持久化队列。
3. **ID 生成**：NextID 支持在 Redis 集群中安全地生成递增 ID。
4. **缓存**：提供函数返回值缓存（redis_cache）和有序字典缓存（CachedOrderedDict）。
5. **概率数据结构**：支持布隆过滤器（BloomFilter）和超穷日志（HyperLogLogs），分别用于成员资格测试和基数估算。
6. **工具**：ContextTimer 用于测量流逝时间。