
---
title: drf-spectacular
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/tfranzel/drf-spectacular?style=social) ](https://github.com/tfranzel/drf-spectacular)
### [tfranzel drf-spectacular](https://github.com/tfranzel/drf-spectacular)

**drf-spectacular** 是一个为 Django REST framework（DRF）生成 OpenAPI 3.0.3/3.1 规范文档的工具，具有以下核心功能和特性：

### **功能与特性**
1. **智能模式生成**  
   自动从 DRF 中提取序列化器、视图、参数等信息，支持复杂嵌套、递归结构，提供灵活的自定义选项（如 `@extend_schema` 装饰器）。
2. **高度可定制**  
   - 支持覆盖请求/响应序列化器、添加参数、定义多态响应、设置示例、调整操作名称等。  
   - 集成第三方库（如 `django-polymorphic`、`SimpleJWT`、`django-filter` 等）。
3. **兼容性与扩展性**  
   - 支持 OpenAPI 3.1，提供国际化、标签分类、认证配置（DRF 原生及自定义）、`SerializerMethodField` 类型推断等。  
   - 可通过 `SpectacularAPIView` 直接在 API 中提供 Schema，并支持 Swagger UI/Redoc 界面。
4. **开箱即用**  
   默认配置可直接使用，仅需安装包、添加 `drf_spectacular` 到 `INSTALLED_APPS`，并设置 `DEFAULT_SCHEMA_CLASS`。

### **使用方法**
1. **安装**  
   ```bash
   pip install drf-spectacular
   ```
2. **配置**  
   ```python
   INSTALLED_APPS = ['drf_spectacular']
   REST_FRAMEWORK = {'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema'}
   ```
3. **设置元数据**  
   ```python
   SPECTACULAR_SETTINGS = {
       'TITLE': '项目名称',
       'DESCRIPTION': '描述',
       'VERSION': '1.0.0',
       # 其他配置如 UI 静态文件路径、验证规则等
   }
   ```
4. **生成 Schema**  
   - 命令行生成文件：  
     ```bash
     python manage.py spectacular --file schema.yml
     ```
   - 在 Django URL 中添加视图：  
     ```python
     path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
     path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
     ```

### **适用场景**
适用于需要生成高质量 OpenAPI 文档的 DRF 项目，尤其适合需自定义参数、多语言支持、集成第三方库的复杂 API 场景。