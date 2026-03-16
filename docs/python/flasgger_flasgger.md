### [flasgger flasgger](https://github.com/flasgger/flasgger)  ![GitHub Repo stars](https://img.shields.io/github/stars/flasgger/flasgger?style=social)

Flasgger 是一款 Flask 扩展，用于从 Flask 视图中提取 OpenAPI 规范并内置 Swagger UI，实现 API 资源的可视化与交互。其核心功能包括：

1.  **多种规范定义**：支持通过文档字符串、外部 YAML 文件、Python 字典或 Marshmallow Schema 定义 API 规格。
2.  **请求数据验证**：基于定义的规范自动验证 POST、PUT、PATCH 等请求的数据有效性。
3.  **生态兼容**：兼容 Flask-RESTful 资源和 Marshmallow APISpec，并支持实验性的 OpenAPI 3.0。
4.  **灵活配置**：支持自定义 Swagger UI 模板、版本、静态资源路径及验证逻辑。