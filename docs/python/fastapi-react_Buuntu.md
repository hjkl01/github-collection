### [Buuntu fastapi-react](https://github.com/Buuntu/fastapi-react)  ![GitHub Repo stars](https://img.shields.io/github/stars/Buuntu/fastapi-react?style=social)

这是一个基于 FastAPI 和 React 的现代化全栈项目启动模板，旨在通过容器化方案快速构建应用程序。

**核心功能：**
1.  **后端服务**：使用 FastAPI (Python 3.8) 提供 API，集成 JWT 认证（OAuth2 密码流）、PostgreSQL 数据库（SQLAlchemy ORM）、Alembic 数据库迁移、Pytest 测试套件以及 Celery 后台任务（配合 Redis 和 Flower 监控）。
2.  **前端应用**：基于 React (TypeScript) 构建，集成 react-router 路由、MaterialUI 样式及 react-admin 管理后台，提供登录、登出、权限控制及 API 交互等辅助功能。
3.  **开发部署**：使用 Docker Compose 管理环境，配置 Nginx 反向代理以统一前后端端口，支持一键构建及测试。

该项目简化了新项目初始化流程，直接提供开箱即用的认证、测试、后台任务处理及生产环境部署基础。