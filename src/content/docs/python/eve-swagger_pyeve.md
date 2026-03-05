
---
title: eve-swagger
---

### [pyeve eve-swagger](https://github.com/pyeve/eve-swagger)  ![GitHub Repo stars](https://img.shields.io/github/stars/pyeve/eve-swagger?style=social)

Eve-Swagger 是为基于 Eve 框架构建的 RESTful API 生成 Swagger 文档的 Python 扩展库。主要功能包括：

1.  **自动生成文档**：扫描 API 配置生成 Swagger JSON，提供 `/api-docs` 端点，兼容 Swagger UI 及编辑器。
2.  **自定义信息**：支持通过配置设置文档标题、版本、描述、联系信息及授权信息。
3.  **字段说明与示例**：支持在 Schema 验证中通过 `description` 和 `example` 属性为字段及资源添加详细说明和示例数据。
4.  **资源控制**：支持禁用特定资源的文档生成，使其不出现在路径或定义中。
5.  **钩子描述**：支持显示 Eve 事件钩子（hooks）的 Docstrings 描述。
6.  **跨域支持**：需配置 CORS 设置以支持 Swagger UI 的跨域请求。