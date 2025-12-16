
---
title: fastapi-cache
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/long2ice/fastapi-cache?style=social) ](https://github.com/long2ice/fastapi-cache)
### [long2ice fastapi-cache](https://github.com/long2ice/fastapi-cache)

**项目功能**  
`fastapi-cache` 是一个为 FastAPI 提供缓存功能的工具，支持通过 Redis、Memcached、DynamoDB 或内存后端缓存接口和函数结果，可自动处理 HTTP 缓存头（如 `ETag`、`Cache-Control`）及条件请求（如 `If-None-Match`）。

**主要特性**  
- 支持多种缓存后端（Redis、Memcached、DynamoDB、内存）。  
- 提供 `@cache` 装饰器，可直接用于 FastAPI 接口或普通函数，支持设置缓存过期时间、命名空间、自定义编码器（如 `JsonCoder` 或 `PickleCoder`）和缓存键生成规则。  
- 自动注入 `Request` 和 `Response` 依赖，支持缓存命中（HIT）或未命中（MISS）状态的响应头标识。  
- 支持自定义数据编码器（`Coder`）和缓存键构建器（`KeyBuilder`），灵活适配复杂数据类型。

**使用方法**  
1. **安装**：通过 `pip install fastapi-cache2` 安装基础包，或添加 `[redis]`、`[memcache]`、`[dynamodb]` 等依赖。  
2. **初始化**：在 FastAPI 启动时调用 `FastAPICache.init()`，传入后端实例（如 `RedisBackend`）及配置（如缓存前缀）。  
3. **装饰器使用**：在接口或函数上使用 `@cache(expire=60)` 设置缓存时间，或通过参数自定义命名空间、编码器等。  
4. **自定义配置**：通过继承 `Coder` 实现自定义编码器，或通过 `key_builder` 参数定义缓存键生成规则（如基于请求路径、查询参数等）。