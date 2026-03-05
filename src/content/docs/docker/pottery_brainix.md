
---
title: pottery
---

### [brainix pottery](https://github.com/brainix/pottery)  ![GitHub Repo stars](https://img.shields.io/github/stars/brainix/pottery?style=social)

Pottery 是一个 Python 库，提供符合 Python 习惯的 Redis 访问方式。它实现了多种 Redis 后端容器（如 RedisDict、RedisSet 等），功能对应 Python 标准库中的 dict、set、list 等类型，使用方式与原生 Python 对象一致。此外，项目还提供分布式锁（Redlock/AIORedlock）、分布式 ID 生成器（NextID）、函数缓存装饰器（redis_cache）、缓存有序字典（CachedOrderedDict）、概率数据结构（BloomFilter、HyperLogLog）及计时工具（ContextTimer）。该项目旨在简化 Redis 使用并支持微服务弹性模式，要求操作数据需可 JSON 序列化。