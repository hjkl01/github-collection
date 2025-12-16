
---
title: flasgger
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/flasgger/flasgger?style=social) ](https://github.com/flasgger/flasgger)
### [flasgger flasgger](https://github.com/flasgger/flasgger)

**Flasgger项目核心内容总结：**  

**项目功能**  
Flasgger是为Flask应用自动生成Swagger（OpenAPI）文档的工具，支持通过路由注释生成API文档、交互式UI界面和静态文件，适用于RESTful API的文档管理。  

**使用方法**  
1. **初始化配置**：通过`Swagger(app)`绑定Flask应用，可自定义模板、Swagger UI版本（2或3）、静态资源路径等。  
2. **路由注释**：在路由函数中添加YAML格式的注释，定义参数、响应结构、示例数据等，Flasgger自动解析生成文档。  
3. **动态数据支持**：使用`LazyString`处理运行时动态值（如根据请求域名或安全状态生成`schemes`字段）。  
4. **反向代理适配**：通过`swaggerUiPrefix`配置解决反向代理环境下“Try it Out”按钮路径错误问题。  

**主要特性**  
- **OpenAPI 3.0支持**：实验性支持OpenAPI 3.0规范，兼容Swagger UI 3版本。  
- **高度可定制**：  
  - 自定义Swagger模板、UI界面、静态资源（如从CDN加载Swagger UI和jQuery）。  
  - 支持`LazyJSONEncoder`处理动态JSON数据。  
- **灵活配置**：  
  - 通过`config`参数设置API信息（如标题、版本、协议）、主机、路径过滤规则等。  
  - 支持提取`id`定义的Schema并复用（如`Palette`和`Color`示例）。  
- **扩展功能**：  
  - HTML sanitizer和Markdown解析器，支持文档中的富文本描述。  
  - 提供默认模板初始化功能，方便集成到现有项目。  

**适用场景**  
适用于需要快速生成、维护并展示Flask API文档的开发场景，尤其适合需要交互式UI和动态配置的项目。