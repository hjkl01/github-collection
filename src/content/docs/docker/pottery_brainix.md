
---
title: pottery
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/brainix/pottery?style=social) ](https://github.com/brainix/pottery)
### [brainix pottery](https://github.com/brainix/pottery)

**项目核心内容总结：**

**功能**  
Pottery 是一个基于 Redis 的 Python 库，提供多种高效数据结构和工具，包括：  
- **缓存装饰器**：通过 `@cached` 实现函数结果缓存，支持自动过期和线程安全。  
- **分布式锁**：使用 `Lock` 防止多线程/多进程并发冲突。  
- **计数器**：通过 `Counter` 实现原子增减操作。  
- **集合操作**：支持 `Set`、`List`、`Dict` 等 Redis 数据结构的增删改查。  
- **高级数据结构**：包括 `BloomFilter`（布隆过滤器）、`HyperLogLog`（基数统计）、`ContextTimer`（计时器）。  

**使用方法**  
1. **安装**：通过 `pip install pottery` 安装。  
2. **缓存**：用 `@cached` 装饰函数，设置 `timeout` 控制过期时间。  
3. **锁**：使用 `Lock(key)` 获取锁，确保临界区安全。  
4. **计数器**：`Counter(key).increment()` 或 `decrement()`。  
5. **BloomFilter**：初始化时指定预计元素数和误判率，用 `add()` 插入元素，`in` 检查是否存在。  
6. **HyperLogLog**：用 `add()` 添加元素，`len()` 估算唯一元素数量。  
7. **ContextTimer**：作为上下文管理器或独立对象，测量代码执行时间（毫秒级）。  

**主要特性**  
- **线程安全**：所有操作均支持多线程/多进程安全。  
- **自动过期**：缓存、锁等支持设置超时时间，避免资源浪费。  
- **高效数据结构**：基于 Redis 实现，适合分布式场景（如 BloomFilter、HyperLogLog）。  
- **轻量灵活**：提供装饰器、类方法等多种使用方式，兼容 Python 标准库接口。  
- **精确控制**：支持自定义 Redis 连接、键名、超时参数等。