
---
title: django-ninja
---

### [vitalik django-ninja](https://github.com/vitalik/django-ninja)

**Django Ninja 核心内容总结：**

**项目功能**  
Django Ninja 是一个基于 Django 和 Python 类型提示的高性能 REST API 框架，支持 OpenAPI 和 JSON Schema 标准，提供自动生成的交互式 API 文档（Swagger UI/Redoc）。

**主要特性**  
- 快速开发：通过类型提示和自动文档生成，减少重复代码。  
- 高性能：利用 Pydantic 和异步支持提升执行速度。  
- 标准兼容：遵循 OpenAPI（原 Swagger）和 JSON Schema 开放标准。  
- 与 Django 深度集成：支持 Django ORM 和核心功能。  
- 生产就绪：已被多家公司用于实际项目。  

**使用方法**  
1. 安装：`pip install django-ninja`  
2. 在 Django 项目中创建 `api.py`，定义路由和逻辑（如示例中的 `/add` 接口）。  
3. 在 `urls.py` 中引入 `api.urls`，通过 `/api/` 路径访问接口。  
4. 访问 `http://127.0.0.1:8000/api/docs` 查看自动生成的 API 文档。  

**文档**  
完整文档地址：https://django-ninja.dev