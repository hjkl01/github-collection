
---
title: postgrest
---

### [postgrest postgrest](https://github.com/postgrest/postgrest)

PostgREST 是一个基于现有 PostgreSQL 数据库自动生成 RESTful API 的工具，可提供符合标准、高性能的接口。其核心功能包括：  
1. **功能**：通过数据库表结构自动生成 REST 接口，支持 CRUD 操作，无需手动编码。  
2. **使用方法**：通过官方文档安装（支持 Docker），运行 `postgrest --help` 查看命令行参数。  
3. **主要特性**：  
   - **高性能**：使用 Haskell 编写，结合 Warp HTTP 服务器和数据库连接池（Hasql），实现高并发与低延迟。  
   - **安全性**：通过 JWT 认证和数据库角色授权，确保操作符合用户权限。  
   - **版本控制**：通过数据库 Schema 实现 API 版本管理，避免接口变更影响应用。  
   - **自文档生成**：基于 OpenAPI 标准生成接口文档，支持 Swagger-UI 等工具展示。  
   - **数据完整性**：依赖 PostgreSQL 约束（如唯一性、外键）保障数据一致性，强制幂等性操作（如 PUT）。