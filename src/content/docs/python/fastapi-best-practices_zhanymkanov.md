
---
title: fastapi-best-practices
---

### [zhanymkanov fastapi-best-practices](https://github.com/zhanymkanov/fastapi-best-practices)  ![GitHub Repo stars](https://img.shields.io/github/stars/zhanymkanov/fastapi-best-practices?style=social)

这是一个提供 FastAPI 生产系统开发最佳实践的指南。内容包括：

1. **项目结构**：推荐按领域（domain）而非文件类型组织代码，保持结构一致且可扩展，类似 Netflix Dispatch 模式。
2. **异步路由**：区分 I/O 密集型与 CPU 密集型任务，避免阻塞事件循环，必要时使用线程池或进程处理。
3. **Pydantic 使用**：充分用于数据验证、自定义序列化模型及配置解耦。
4. **依赖注入**：利用 FastAPI 依赖项进行请求验证、逻辑复用和性能优化（依赖结果在请求范围内缓存）。
5. **其他规范**：
    - 遵循 REST 风格，统一资源命名。
    - 优化响应序列化流程。
    - 管理 API 文档（环境隔离显示）。
    - 统一数据库表名、索引命名及迁移规范（Alembic）。
    - 优先在 SQL 层处理复杂数据聚合（SQL-first）。
    - 从第一天起使用异步测试客户端。
    - 使用 Ruff 替代多个工具进行代码检查和格式化。