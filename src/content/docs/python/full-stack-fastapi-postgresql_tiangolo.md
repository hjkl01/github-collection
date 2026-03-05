
---
title: full-stack-fastapi-postgresql
---

### [tiangolo full-stack-fastapi-postgresql](https://github.com/tiangolo/full-stack-fastapi-postgresql)  ![GitHub Repo stars](https://img.shields.io/github/stars/tiangolo/full-stack-fastapi-postgresql?style=social)

这是一个基于 FastAPI 和 React 的全栈 Web 应用开发模板，核心功能总结如下：

- **后端服务**：采用 FastAPI 作为 API 框架，SQLModel 进行 ORM 操作，PostgreSQL 作为数据库，内置 JWT 认证、密码哈希及邮件密码恢复功能。
- **前端界面**：使用 React、TypeScript 和 Vite 构建，集成 Tailwind CSS 和 shadcn/ui 组件库，支持暗色模式及自动生成的 API 客户端。
- **部署与运维**：支持 Docker Compose 进行开发和生产环境部署，通过 Traefik 实现反向代理与自动 HTTPS 证书管理，配备 GitHub Actions CI/CD 流水线。
- **测试与质量**：包含 Pytest 后端测试和 Playwright 端到端测试，提供交互式 API 文档。
- **项目初始化**：支持直接克隆仓库或通过 Copier 工具快速生成项目，需配置环境变量（如密钥、数据库密码）即可运行。