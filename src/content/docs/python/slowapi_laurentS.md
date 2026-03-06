
---
title: slowapi
---

### [laurentS slowapi](https://github.com/laurentS/slowapi)  ![GitHub Repo stars](https://img.shields.io/github/stars/laurentS/slowapi?style=social)

SlowApi 是适配 Starlette 和 FastAPI 的速率限制库。
主要功能：
1. 通过装饰器对 HTTP 端点实施单重或多重限流。
2. 支持 Redis、Memcached 和内存作为限流存储后端。
3. 兼容同步和异步 HTTP 端点，支持跨路由共享限流策略。
使用限制：
1. 端点函数需显式接收 request 参数。
2. 暂不支持 WebSocket 端点。