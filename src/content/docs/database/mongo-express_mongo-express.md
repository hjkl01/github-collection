
---
title: mongo-express
---

### [mongo-express mongo-express](https://github.com/mongo-express/mongo-express)

**Mongo Express 是一个用于 MongoDB 的 Web 管理工具，支持数据库查询、文档编辑、数据管理等操作。**  

**核心功能：**  
- 提供简单和高级搜索功能，支持 MongoDB 查询语法；  
- 支持多种 BSON 数据类型（如 ObjectId、ISODate、UUID、Binary 等）的编辑与展示；  
- 可通过 Docker 快速部署，支持 IBM Cloud 和 OpenID Connect 认证；  
- 支持 SSL 加密、GridFS 文件管理、自定义分页显示等特性；  
- 可作为独立应用运行，或集成到其他项目中作为中间件使用。  

**使用方法：**  
1. **独立运行**：修改 `config.js` 配置数据库连接、认证信息，启动服务后通过浏览器访问 `http://localhost:8081`；  
2. **Docker 部署**：通过环境变量配置 MongoDB 连接和认证参数，运行镜像即可；  
3. **云平台部署**：支持 IBM Cloud 手动或自动部署，需配置对应服务和环境变量；  
4. **OpenID Connect 认证**：需安装 `express-openid-connect` 依赖，并设置 Identity Provider 的相关参数。  

**主要特性：**  
- 支持复杂数据类型（如代码、时间戳、符号等）的可视化编辑；  
- 提供文档导入、导出、删除确认等交互功能；  
- 通过环境变量灵活配置 SSL、认证、端口等参数；  
- 支持 Docker Extensions 一键部署（需 Docker Desktop 4.15+）。  

**注意事项：**  
- 项目仅适用于开发环境，**禁止在生产环境中使用**，因 Web 界面可能执行恶意 JavaScript；  
- 二进制数据类型（Binary/BinData）未经过充分测试。