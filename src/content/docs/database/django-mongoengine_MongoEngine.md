
---
title: django-mongoengine
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/MongoEngine/django-mongoengine?style=social) ](https://github.com/MongoEngine/django-mongoengine)
### [MongoEngine django-mongoengine](https://github.com/MongoEngine/django-mongoengine)

**项目核心内容总结：**

**功能**  
Django-MongoEngine 是一个将 Django 与 MongoEngine 结合的库，支持 Django 4.2，提供会话管理、模型/字段、视图、认证等功能，但管理界面（admin）仅实现基础功能，部分功能不完善。

**使用方法**  
1. 在 `settings.py` 中配置 MongoDB 数据库连接信息，并添加 `django_mongoengine` 到 `INSTALLED_APPS`。  
2. 文档类继承自 `django_mongoengine.Document`，字段使用 `django_mongoengine.fields` 定义（如 `StringField`、`EmbeddedDocumentField` 等）。  
3. 启用 MongoDB 会话需设置 `SESSION_ENGINE = 'django_mongoengine.sessions'` 及 `SESSION_SERIALIZER`。

**主要特性**  
- 字段默认可选（使用 `required=False`，兼容 MongoEngine 风格）。  
- 部分代码通过继承、重用或猴子补丁实现，非直接复制 Django 代码。  
- 项目处于不稳定状态，可能因 Django 更新而失效，不推荐用于新项目，建议使用 `django-mongodb-backend`。

**注意事项**  
- 项目不稳定，存在兼容性风险，部分功能（如 admin）未完全测试。  
- 需自行处理文档同步、调试工具集成等任务。