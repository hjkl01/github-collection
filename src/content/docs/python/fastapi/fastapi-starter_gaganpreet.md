
---
title: fastapi-starter
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/gaganpreet/fastapi-starter?style=social) ](https://github.com/gaganpreet/fastapi-starter)
### [gaganpreet fastapi-starter](https://github.com/gaganpreet/fastapi-starter)

**项目核心内容总结：**

**项目功能**  
FastAPI-Starter 是一个基于 FastAPI 的项目模板，集成 FastAPI Users（用户认证）、React-Admin（管理界面）、OpenAPI Generator（生成 TypeScript 客户端）、SQLAlchemy 2.0（异步数据库操作）等工具，支持自动化测试、Docker 部署及代码规范管理。

**使用方法**  
1. 安装 Python 3 和 pip，通过 Cookiecutter 生成项目：  
   ```bash  
   pip3 install cookiecutter  
   cookiecutter https://github.com/gaganpreet/fastapi-starter  
   ```  
2. 可选使用 Cruft 工具更新模板：  
   ```bash  
   cruft create https://github.com/gaganpreet/fastapi-starter  
   cruft update  
   ```  

**主要特性**  
- 采用工厂模式与环境变量配置，遵循最佳实践  
- 自动生成 TypeScript 客户端代码，无需手动维护  
- 异步优先架构（SQLAlchemy 2.0 + Alembic 数据库迁移）  
- 包含 pytest 单元测试、Cypress 集成测试  
- Docker 镜像支持（前后端分离及合并部署方案）  
- 代码规范工具链（Black、isort、flake8、Prettier、ESLint）  
- 自动化 CI/CD 流程（GitHub Actions 构建镜像、Dependabot 依赖更新）