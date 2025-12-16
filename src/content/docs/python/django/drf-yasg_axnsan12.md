
---
title: drf-yasg
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/axnsan12/drf-yasg?style=social) ](https://github.com/axnsan12/drf-yasg)
### [axnsan12 drf-yasg](https://github.com/axnsan12/drf-yasg)

**项目核心内容总结：**  
drf-yasg 是一个为 Django Rest Framework（DRF）生成 Swagger/OpenAPI 2.0 规范的工具，支持自动生成 API 文档并集成交互式 UI（如 swagger-ui 和 redoc）。  

**主要功能：**  
- 自动生成 API 文档，支持嵌套序列化器、响应模式、模型定义等；  
- 支持 JSON/YAML 格式输出，内置 swagger-ui 和 redoc 查看工具；  
- 支持 DRF 的版本控制（如 URL 路由版本）；  
- 提供验证功能（如语法校验、兼容代码生成工具）；  
- 集成第三方库（如 djangorestframework-camel-case、drf-extra-fields）。  

**使用方法：**  
1. 安装：`pip install drf-yasg`；  
2. 在 `settings.py` 中添加 `drf_yasg` 到 `INSTALLED_APPS`；  
3. 在 `urls.py` 中配置 `get_schema_view`，定义文档访问路径（如 `/swagger/`）；  
4. 启动服务后，通过浏览器访问生成的文档页面。  

**主要特性：**  
- 支持 Django 3.2+、DRF 3.14+、Python 3.9-3.13；  
- 提供缓存机制提升性能；  
- 支持通过 `swagger-cli` 或在线工具验证规范合法性；  
- 兼容第三方扩展（如 camelCase 字段格式处理）。