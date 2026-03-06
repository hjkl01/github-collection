
---
title: fastapi-best-practices
---

### [zhanymkanov fastapi-best-practices](https://github.com/zhanymkanov/fastapi-best-practices)  ![GitHub Repo stars](https://img.shields.io/github/stars/zhanymkanov/fastapi-best-practices?style=social)

本项目是一套 FastAPI 生产环境最佳实践指南，总结了构建生产系统的经验教训。核心内容包括：

1.  **项目结构**：推荐基于领域模块组织代码，提升大型单体应用的扩展性。
2.  **异步处理**：区分 I/O 密集型与 CPU 密集型任务的处理策略，防止事件循环阻塞。
3.  **模型与验证**：深度使用 Pydantic 进行数据校验与转换，自定义基础模型并解耦配置。
4.  **依赖注入**：支持依赖链、缓存复用及异步依赖，用于复杂的请求验证与逻辑复用。
5.  **工程规范**：涵盖 REST 规范、响应序列化优化、同步 SDK 线程池处理、异常处理、文档配置、数据库命名与迁移、SQL 优先查询、异步测试及代码检查工具（Ruff）的使用。

旨在通过标准化规范提升开发体验与系统质量。