
---
title: cookiecutter-django
---

### [cookiecutter cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django)  ![GitHub Repo stars](https://img.shields.io/github/stars/cookiecutter/cookiecutter-django?style=social)

Cookiecutter Django 是一个基于 Cookiecutter 的框架，用于快速生成生产就绪的 Django 项目。主要功能总结：

- **基础支持**：支持 Django 5.2 和 Python 3.13，项目生成时即包含 100% 测试覆盖。
- **标准配置**：默认集成 Bootstrap 5 前端、PostgreSQL 数据库，遵循 12-Factor 环境配置原则，默认启用 SSL 安全策略。
- **核心功能**：内置基于 django-allauth 的用户注册、自定义用户模型、邮件发送服务（Anymail）及多种云存储（S3/Google/Azure）支持。
- **部署与容器化**：提供 Docker 开发及生产环境配置（含 Traefik/LetsEncrypt），支持 Heroku、PythonAnywhere 等平台部署。
- **可选集成**：支持集成 Celery、Sentry、Gulp/Webpack、异步 ASGI 及邮件测试工具等。
- **快速生成**：通过命令行交互配置，快速生成标准化、可定制的 Django 项目结构。