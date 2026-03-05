
---
title: django-mongoengine
---

### [MongoEngine django-mongoengine](https://github.com/MongoEngine/django-mongoengine)  ![GitHub Repo stars](https://img.shields.io/github/stars/MongoEngine/django-mongoengine?style=social)

该项目旨在让 Django 应用使用 MongoDB 作为数据库后端，通过 MongoEngine 实现集成。核心功能支持基于 MongoDB 的 Session、模型字段、视图、认证及部分管理后台功能。使用时需在配置中设置 MongoDB 连接并启用 django_mongoengine 应用，字段定义采用 MongoEngine 风格（默认所有字段可选）。由于项目目前状态不稳定且易随 Django 更新而失效，不建议用于新项目，推荐改用 django-mongodb-backend。