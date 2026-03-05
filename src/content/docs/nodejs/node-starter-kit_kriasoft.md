
---
title: node-starter-kit
---

### [kriasoft node-starter-kit](https://github.com/kriasoft/node-starter-kit)  ![GitHub Repo stars](https://img.shields.io/github/stars/kriasoft/node-starter-kit?style=social)

这是一个专为服务器端架构（如 Google Cloud Functions、AWS Lambda）优化的 Node.js API 项目模板，可用于构建后端应用。

主要功能包括：
- **数据库管理**：支持数据库优先设计，自动生成强类型 TypeScript 数据模型，包含迁移、种子数据和 REPL 工具。
- **认证授权**：集成 OAuth 2.0 提供商（Google、Facebook 等），使用 JWT 和会话 Cookie 实现无状态会话。
- **API 开发**：提供基于代码优先方法的 GraphQL API 示例。
- **工程化支持**：预配置 Jest 单元测试、Rollup 应用捆绑、结构化日志及错误报告。
- **环境与部署**：支持本地热重载，配置多环境（本地、开发、测试、生产），并提供云端部署脚本。

核心依赖技术包括 Node.js、TypeScript、PostgreSQL、GraphQL 和 Knex。