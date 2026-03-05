
---
title: slowapi
---

### [laurentS slowapi](https://github.com/laurentS/slowapi)  ![GitHub Repo stars](https://img.shields.io/github/stars/laurentS/slowapi?style=social)

SlowApi 是一个基于 limits 库并适配自 flask-limiter 的 Starlette 和 FastAPI 限流库。支持同步和异步 HTTP 端点限流，提供 Redis、Memcached 及内存等多种存储后端，支持单/多限流装饰器配置及跨路由共享限流。使用限制为需在端点中显式传入 request 对象，暂不支持 WebSocket 端点。