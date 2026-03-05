
---
title: cookiecutter-django
---

### [pydanny cookiecutter-django](https://github.com/pydanny/cookiecutter-django)  ![GitHub Repo stars](https://img.shields.io/github/stars/pydanny/cookiecutter-django?style=social)

Cookiecutter Django 是一个基于 Cookiecutter 的脚手架框架，用于快速生成生产级别的 Django 项目。

核心功能：
- 支持 Django 5.2 和 Python 3.13，预设 100% 测试覆盖率及 12-Factor 环境配置。
- 默认启用 SSL 安全，内置 django-allauth 用户注册及自定义用户模型。
- 提供 Docker 开发与生产部署（含 Traefik/LetsEncrypt），支持 Heroku 和 PythonAnywhere，集成 pre-commit。
- 默认使用 PostgreSQL，集成 Bootstrap 5、Anymail 邮件服务及多种云存储方案。
- 可选支持 Celery、Sentry、Mailpit、Websockets 及前端静态文件构建。

通过命令行交互引导初始化，自动化生成结构规范的项目。