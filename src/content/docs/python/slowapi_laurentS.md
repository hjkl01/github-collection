
---
title: slowapi
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/laurentS/slowapi?style=social) ](https://github.com/laurentS/slowapi)
### [laurentS slowapi](https://github.com/laurentS/slowapi)

**核心内容总结：**  
SlowApi 是一个为 Starlette 和 FastAPI 设计的限流库，基于 Flask-Limiter 改编，适用于生产环境，支持处理高并发请求。  

**功能与使用方法：**  
- 通过装饰器（如 `@limiter.limit("5/minute")`）为 API 端点设置限流规则。  
- 支持 Redis、Memcached 和内存作为限流存储后端（内存为默认后备）。  
- 兼容同步和异步 HTTP 端点。  
- 可跨多个路由共享限流规则。  
- 安装方式：`pip install slowapi`。  

**主要特性：**  
- 支持所有当前主流 Python 版本。  
- 提供详细的文档（[Read the Docs](https://slowapi.readthedocs.io/en/latest/)）。  

**注意事项：**  
- 端点函数必须显式接收 `request: Request` 参数，否则无法生效。  
- 当前不支持 WebSocket 端点。  

**开发与贡献：**  
- 使用 Poetry 管理依赖，通过 `pytest` 运行测试。  
- 欢迎提交 PR，需包含对应测试用例。