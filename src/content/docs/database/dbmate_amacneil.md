
---
title: dbmate
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/amacneil/dbmate?style=social) ](https://github.com/amacneil/dbmate)
### [amacneil dbmate](https://github.com/amacneil/dbmate)

**项目核心内容总结：**

**功能：**  
dbmate 是一个支持多数据库（PostgreSQL、MySQL、SQLite、ClickHouse）的轻量级数据库迁移工具，提供纯 SQL 迁移文件管理、数据库创建/删除、模式备份、环境变量自动加载等功能。

**使用方法：**  
1. **CLI 命令**：通过 `dbmate new` 创建迁移文件，`dbmate up` 应用迁移，`dbmate down` 回滚。  
2. **库集成**：支持以 Go 库形式嵌入应用，通过 `embed` 功能加载迁移文件。  
3. **配置**：通过环境变量或连接字符串指定数据库参数，无需额外配置文件。

**主要特性：**  
- 支持时间戳版本的迁移文件（如 `20231001_create_table.sql`）。  
- 自动创建 `schema_migrations` 表记录迁移状态，支持自定义表名。  
- 提供 `schema.sql` 完整模式备份文件，可直接用于数据库恢复。  
- 内置等待数据库就绪功能，适用于容器化部署场景。  
- 语言/框架无关，兼容主流数据库，无需依赖 ORM。