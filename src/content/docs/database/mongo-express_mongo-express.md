
---
title: mongo-express
---

### [mongo-express mongo-express](https://github.com/mongo-express/mongo-express)  ![GitHub Repo stars](https://img.shields.io/github/stars/mongo-express/mongo-express?style=social)

mongo-express 是一个基于 Node.js、Express 和 Bootstrap 5 构建的 MongoDB Web 管理界面，适用于 MongoDB 及兼容服务（如 FerretDB、Amazon DocumentDB）。

主要功能：
1. **多数据库管理**：支持连接多个数据库，查看、添加、删除数据库。
2. **集合与文档操作**：支持查看、添加、重命名、删除集合；支持查看、添加、更新、删除文档，并支持多种 BSON 数据类型（如 ObjectId、ISODate、UUID 等）。
3. **媒体与文件处理**：支持音频、视频、图片内联预览；支持 GridFS 存储和读取大文件。
4. **性能与体验**：大对象异步加载，嵌套对象折叠展示；响应式设计适配移动端。
5. **安全与认证**：支持基本认证和 OpenIdConnect；支持数据库白名单/黑名单；支持 TLS/SSL 配置。
6. **部署灵活**：支持 npm 全局/本地安装、CLI 运行、Express 中间件集成及 Docker 容器部署。

安全提示：由于 JSON 解析涉及 JavaScript 执行，存在安全风险，仅限私有的开发环境使用。