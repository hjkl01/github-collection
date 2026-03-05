
---
title: fastapi-cache
---

### [long2ice fastapi-cache](https://github.com/long2ice/fastapi-cache)  ![GitHub Repo stars](https://img.shields.io/github/stars/long2ice/fastapi-cache?style=social)

`fastapi-cache`（包名 `fastapi-cache2`）是一款支持 Redis、Memcached、DynamoDB 及内存后端的 FastAPI 缓存插件。它通过 `@cache` 装饰器提供端点和函数的透明缓存，支持 `ETag`、`Cache-Control` 等 HTTP 缓存头及条件请求，允许自定义过期时间、命名空间、数据编解码器和键生成逻辑，并能自动注入依赖以管理缓存状态。