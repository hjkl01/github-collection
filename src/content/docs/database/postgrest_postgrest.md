
---
title: postgrest
---

### [postgrest postgrest](https://github.com/postgrest/postgrest)  ![GitHub Repo stars](https://img.shields.io/github/stars/postgrest/postgrest?style=social)

PostgREST 是为现有 PostgreSQL 数据库自动生成完全 RESTful API 的服务。相比手写 API，它更清洁、标准且高效。项目基于 Haskell 编写，将计算逻辑（如验证、授权、JSON 序列化）委托给数据库以优化性能。它支持 JWT 认证和数据库角色授权，利用 Schema 进行 API 版本控制，并通过 OpenAPI 标准自动生成文档。此外，系统依赖数据库声明性约束确保数据完整性，防止应用层代码破坏数据。