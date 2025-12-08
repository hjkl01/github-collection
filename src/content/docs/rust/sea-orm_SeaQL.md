
---
title: sea-orm
---

### [SeaQL sea-orm](https://github.com/SeaQL/sea-orm)

**SeaORM 核心内容总结：**

1. **项目功能**  
   SeaORM 是一个基于 Rust 的异步 ORM 框架，支持 PostgreSQL、MySQL、SQLite 等主流数据库，提供类型安全的数据库操作、数据库迁移工具、灵活的查询构建器等功能，适用于 Web 开发和数据密集型应用。

2. **使用方法**  
   - 通过 Derive 宏自动生成模型类。  
   - 使用 SeaQuery API 构建类型安全的 SQL 查询。  
   - 通过迁移工具管理数据库 schema 变更。  
   - 支持与 Actix-web、Rocket 等 Rust Web 框架集成。

3. **主要特性**  
   - **类型安全**：编译时检查 SQL 查询，避免运行时错误。  
   - **异步支持**：基于 Tokio，适用于高并发场景。  
   - **数据库迁移**：提供迁移工具和版本控制功能。  
   - **灵活查询**：支持 ActiveRecord 模式和手动 SQL 构建。  
   - **社区生态**：集成 SeaQuery（SQL 构建器）、Seaography（GraphQL 框架）等工具。

4. **版本更新**  
   SeaORM 2.0 引入新特性，包括实体优先工作流、强类型列定义、RBAC（基于角色的访问控制）支持，以及改进的开发体验。