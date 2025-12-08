
---
title: node-starter-kit
---

### [kriasoft node-starter-kit](https://github.com/kriasoft/node-starter-kit)

**Node.js API Starter Kit 核心内容总结**

**项目功能**  
提供一个基于 Node.js 的 API 开发模板，适配 Google Cloud Functions、AWS Lambda 等无服务器架构，支持构建后端服务及前端应用接口。包含数据库模型生成、OAuth 2.0 认证、JWT 无状态会话、GraphQL API、数据库迁移、测试框架、云部署等功能。

**主要特性**  
- 数据库优先设计，自动生成 TypeScript 类型安全模型  
- 支持 Google/Facebook/GitHub 等 OAuth 2.0 登录  
- 基于 JWT 的无状态会话（兼容 SSR）  
- GraphQL API 示例（代码优先开发方式）  
- 数据库迁移、种子数据及 REPL 工具  
- 使用 Handlebars 的邮件模板及预览功能  
- 集成 Jest/Supertest 等测试框架  
- 支持 Docker 和 Google Cloud 部署  

**使用方法**  
1. 克隆项目，安装依赖（`yarn install`）  
2. 配置环境变量（`./env/.env.*` 文件）  
3. 启动本地服务（`yarn start`）  
4. 通过 `yarn deploy` 部署到 Google Cloud Functions  
5. 部署前需配置 Google Cloud CLI、创建 GCP 项目及 Cloud SQL 数据库