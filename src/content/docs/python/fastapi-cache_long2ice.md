
---
title: fastapi-cache
---

### [long2ice fastapi-cache](https://github.com/long2ice/fastapi-cache)  ![GitHub Repo stars](https://img.shields.io/github/stars/long2ice/fastapi-cache?style=social)

fastapi-cache 是一个用于缓存 FastAPI 端点和函数结果的 Python 工具库。支持 Redis、Memcached、DynamoDB 及内存等多种后端。核心功能包括：通过@cache 装饰器集成缓存逻辑；支持 HTTP 缓存头（如 ETag、Cache-Control）及条件请求处理；可配置过期时间、命名空间、自定义编解码器及缓存键生成规则；自动注入请求和响应依赖，支持 Pydantic 等数据类型的序列化与还原。