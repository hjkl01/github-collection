
---
title: swagger-ui
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/swagger-api/swagger-ui?style=social) ](https://github.com/swagger-api/swagger-ui)
### [swagger-api swagger-ui](https://github.com/swagger-api/swagger-ui)

**核心内容总结：**  
Swagger UI 是一个基于 OpenAPI 规范自动生成 API 文档的工具，支持可视化交互 API 接口，适用于开发、测试和文档展示。  

**功能与使用方法：**  
1. **项目功能**：根据 OpenAPI 规范自动生成 API 文档，提供交互式界面测试接口，支持多种前端框架（如 React、Vue）。  
2. **模块使用**：提供三个 NPM 模块：  
   - `swagger-ui`：适用于单页应用，需依赖解析。  
   - `swagger-ui-dist`：适用于无法解析依赖的项目，直接使用静态资源。  
   - `swagger-ui-react`：集成 React 框架。  
3. **兼容性**：支持 OpenAPI 3.0 规范，但部分功能（如 JSON 表单编辑器、多语言支持）未完全实现。  

**主要特性：**  
- 支持多种认证方式（OAuth2、API Key）。  
- 提供丰富的 UI 组件和交互功能。  
- 可定制主题和布局。  

**注意事项：**  
- **已知限制**：部分参数支持不完整，外部文件相对路径功能未实现。  
- **安全问题**：需通过邮件（security@swagger.io）披露漏洞，而非公开问题跟踪器。  
- **浏览器支持**：仅兼容最新版 Chrome、Safari、Firefox 和 Edge。