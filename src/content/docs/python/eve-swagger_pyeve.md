
---
title: eve-swagger
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/pyeve/eve-swagger?style=social) ](https://github.com/pyeve/eve-swagger)
### [pyeve eve-swagger](https://github.com/pyeve/eve-swagger)

**项目核心内容总结：**  
Eve-Swagger 是一个为 Eve 框架的 RESTful API 自动生成 Swagger 文档的扩展工具，帮助开发者快速构建 API 接口说明文档。  

**主要功能：**  
1. **Swagger 文档生成**：通过配置 `SWAGGER_INFO` 自动生成符合 Swagger 2.0 规范的 JSON 文档，支持自定义标题、版本、描述、协议等信息。  
2. **动态扩展文档**：运行时可通过 `add_documentation` 方法动态添加或修改接口参数说明。  
3. **资源级禁用文档**：在 `settings.py` 中设置 `disable_documentation: True` 可隐藏特定资源的接口说明。  
4. **事件钩子描述**：启用 `ENABLE_HOOK_DESCRIPTION` 后，可将 Eve 事件钩子（如 `on_pre_GET`）的注释显示在 Swagger 文档中。  
5. **字段与资源示例**：支持为字段或资源添加 `description` 和 `example` 字段，用于 Swagger UI 展示，需自定义 Cerberus 验证器以避免报错。  

**使用方法：**  
- 安装：`pip install eve-swagger`  
- 配置：在 Eve 应用中注册 Swagger 蓝图，设置 `SWAGGER_INFO` 和 `SWAGGER_HOST`，并根据需要添加自定义验证器或文档内容。  
- 访问 `/api-docs` 端点获取生成的 JSON 文档，配合 Swagger UI 或 Editor 使用。  

**注意事项：**  
- 若 Swagger UI 报跨域错误，需在 Eve 的 `settings.py` 中配置 `X_DOMAINS` 和 `X_HEADERS`。  
- 使用 `description` 或 `example` 字段时，需继承 `Validator` 类并重写验证方法，否则会触发 Cerberus 错误。  
- 可通过 `SWAGGER_EXAMPLE_FIELD_REMOVE` 配置项禁用 `example` 属性的生成。