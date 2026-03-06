
---
title: django-mongoengine
---

### [MongoEngine django-mongoengine](https://github.com/MongoEngine/django-mongoengine)  ![GitHub Repo stars](https://img.shields.io/github/stars/MongoEngine/django-mongoengine?style=social)

Django-MongoEngine 是一个基于 MongoEngine 实现的 Django 与 MongoDB 集成项目。目前状态不稳定，不建议用于新项目，但支持 Django 4.2 的模型、字段、视图、认证及基础 Admin 功能。项目提供 MongoDB 会话后端，用户需继承 `django_mongoengine.Document` 定义模型，字段参数兼容 MongoEngine 风格且默认均为可选。