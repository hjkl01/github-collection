
---
title: go-redis
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/redis/go-redis?style=social) ](https://github.com/redis/go-redis)
### [redis go-redis](https://github.com/redis/go-redis)

**核心内容总结：**

go-redis 是一个用于 Go 语言的 Redis 客户端库，支持 Redis 的所有核心功能，包括集群、管道操作、事务处理等。其主要特性包括：  
1. **功能全面**：支持 Redis 的所有常用命令（如 SET、GET、SORT、ZINTERSTORE 等），并提供类型化错误处理（如认证失败、集群异常等）。  
2. **高效连接管理**：内置连接池，支持自定义缓冲区大小（默认 32KiB），优化高吞吐场景性能。  
3. **集群与管道支持**：提供集群客户端配置，支持管道（Pipeline）批量操作及事务（Transaction）处理。  
4. **可扩展性**：允许通过自定义钩子（Hook）实现日志记录、错误包装、请求上下文处理等功能。  
5. **开发友好**：提供丰富的使用示例（如 Eval 脚本、自定义命令），支持 Docker 测试环境快速运行。  

**使用方法**：通过 `go get` 安装后，可直接使用 `redis.NewClient` 连接 Redis，调用对应方法执行命令。支持集群模式配置、管道操作（`Pipeline().Exec()`）及事务（`Multi()`）。  

**适用场景**：适用于需要高性能、稳定连接 Redis 的 Go 项目，尤其适合分布式系统、高并发场景。