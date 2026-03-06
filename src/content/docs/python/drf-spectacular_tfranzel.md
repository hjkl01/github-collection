
---
title: drf-spectacular
---

### [tfranzel drf-spectacular](https://github.com/tfranzel/drf-spectacular)  ![GitHub Repo stars](https://img.shields.io/github/stars/tfranzel/drf-spectacular?style=social)

drf-spectacular 是一个为 Django REST Framework (DRF) 生成 OpenAPI (3.0.3 & 3.1) 规范的 Python 库。核心功能包括：

1. 自动从 DRF 序列化器提取 Schema，支持组件化、嵌套和递归。
2. 提供 `@extend_schema` 装饰器，支持自定义视图、参数、请求/响应序列化器及多态响应。
3. 支持身份验证、i18n、标签提取、文档注释解析及 Vendor 扩展。
4. 集成 Swagger UI 和 Redoc 视图，支持命令行生成 Schema 文件。
5. 兼容多种 DRF 扩展库（如 SimpleJWT、django-filter、Pydantic 等）。