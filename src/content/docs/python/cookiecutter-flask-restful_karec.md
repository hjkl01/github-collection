
---
title: cookiecutter-flask-restful
---

### [karec cookiecutter-flask-restful](https://github.com/karec/cookiecutter-flask-restful)  ![GitHub Repo stars](https://img.shields.io/github/stars/karec/cookiecutter-flask-restful?style=social)

这是一个基于 Cookiecutter 的 Flask REST API 项目模板，用于快速构建 REST 服务。
核心功能包括：
1. 项目结构：采用应用工厂模式与蓝图，支持环境变量配置及 Flask CLI 集成。
2. 技术栈：集成 Flask-RESTful、SQLAlchemy、Marshmallow、JWT 认证（含访问与刷新令牌）及数据库迁移。
3. 文档支持：内置 OpenAPI/Swagger/ReDoc 文档生成与展示。
4. 测试与扩展：支持 pytest/factoryboy 单元测试，可选集成 Celery 任务队列。
5. 部署能力：提供 Docker/docker-compose 及 Makefile 支持，兼容 Gunicorn/uWSGI 等 WSGI 服务器。