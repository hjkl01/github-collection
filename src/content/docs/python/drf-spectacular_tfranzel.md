
---
title: drf-spectacular
---

### [tfranzel drf-spectacular](https://github.com/tfranzel/drf-spectacular)  ![GitHub Repo stars](https://img.shields.io/github/stars/tfranzel/drf-spectacular?style=social)

drf-spectacular 是一款适用于 Django REST framework 的 OpenAPI 模式生成器，支持 OpenAPI 3.0.3 及 3.1 标准。它旨在自动提取 DRF 架构信息并提供灵活性，以生成兼容主流客户端生成器的模式。主要功能包括：序列化器组件化（支持嵌套与递归）、使用 `@extend_schema` 装饰器自定义视图参数与响应、支持认证、类型提示、i18n、标签及示例提取。内置 Swagger-UI 和 Redoc 服务视图，并兼容多种第三方库（如 SimpleJWT、django-filter、Pydantic 等）。通过配置 Settings 即可快速集成使用。