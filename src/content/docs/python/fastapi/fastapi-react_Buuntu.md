
---
title: fastapi-react
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/Buuntu/fastapi-react?style=social) ](https://github.com/Buuntu/fastapi-react)
### [Buuntu fastapi-react](https://github.com/Buuntu/fastapi-react)

**项目核心内容总结：**

本项目是一个基于 FastAPI（Python）和 React（TypeScript）的全栈开发模板，集成现代技术栈，提供开箱即用的功能，包括：

- **核心功能：**
  - 后端使用 FastAPI 实现 JWT 认证、SQLAlchemy ORM、PostgreSQL 数据库、Celery + Redis 后台任务、Alembic 数据库迁移。
  - 前端使用 React + TypeScript + MaterialUI，包含路由管理、认证工具函数、私有路由高阶组件。
  - 管理后台基于 react-admin，与后端 JWT 认证无缝集成。

- **开发特性：**
  - 提供 Docker Compose 开发环境，集成 Nginx 反向代理（支持前后端同端口部署）。
  - 包含 Pytest 测试框架，支持测试数据库、事务回滚及可复用的测试用例（如 `test_db`、`client`、`user_token_headers` 等）。
  - 支持后台任务监控（通过 Flower）。

- **使用方法：**
  1. 安装 cookiecutter 和 docker-compose。
  2. 通过 `cookiecutter gh:Buuntu/fastapi-react` 创建项目，填写配置参数。
  3. 执行 `./scripts/build.sh` 构建镜像并启动容器。
  4. 访问 `localhost:端口` 查看前端页面，通过 `/admin` 路径使用 react-admin 管理后台（需超级用户登录）。

- **附加功能：**
  - 前端认证工具（如 `login`、`logout`、`isAuthenticated`）及私有路由保护。
  - 支持部署到 Docker Swarm 模式，结合 Nginx 实现 HTTPS 自动证书管理。