
---
title: cookiecutter-flask
---

### [cookiecutter-flask cookiecutter-flask](https://github.com/cookiecutter-flask/cookiecutter-flask)  ![GitHub Repo stars](https://img.shields.io/github/stars/cookiecutter-flask/cookiecutter-flask?style=social)

这是一个基于 Cookiecutter 的 Flask 项目生成模板，支持 Python 3.8 及以上版本。

核心功能如下：
1. **项目生成**：支持 Docker（推荐）和标准 pip 方式快速创建 Flask 项目结构。
2. **前端资源**：集成 Bootstrap 5、Font Awesome 6 前端模板，使用 Webpack 进行 CSS/JS 打包及 npm 管理。
3. **后端功能**：包含基础用户模型，集成 Flask-SQLAlchemy 数据库、Flask-Migrate 迁移、Flask-Login 认证、Flask-WTForms 表单及 Flask-Bcrypt 密码加密。
4. **开发部署**：遵循 Twelve-Factor App 环境配置规范，支持 pytest 测试、Factory-Boy 模拟、Flask Click CLI 命令及 Heroku PaaS 部署。
5. **架构模式**：采用 Blueprint 和 Application Factory 最佳实践，附带调试工具和缓存功能。