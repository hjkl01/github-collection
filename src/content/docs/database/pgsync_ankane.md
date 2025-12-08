
---
title: pgsync
---

### [ankane pgsync](https://github.com/ankane/pgsync)

**核心内容总结：**  

**功能**  
pgsync 是一个用于在两个 PostgreSQL 数据库之间同步数据的工具，功能类似于 `pg_dump`/`pg_restore`，支持快速、安全、灵活的数据迁移。  

**主要特性**  
- **速度**：通过并行传输加速数据同步。  
- **安全性**：内置规则防止敏感数据泄露（如替换为随机值或隐藏字段）。  
- **灵活性**：兼容源库与目标库的 schema 差异（如列缺失、列多余）。  
- **便利性**：支持同步部分表、表组、关联记录，提供过滤条件（如 `where store_id = 1`）。  

**使用方法**  
1. **安装**：通过 `gem install pgsync`、Homebrew 或 Docker 安装。  
2. **配置**：运行 `pgsync --init` 生成 `.pgsync.yml` 文件，定义源库、目标库、排除表、敏感数据规则等。  
3. **同步数据**：  
   - 默认同步所有表：`pgsync`  
   - 指定表：`pgsync table1,table2`  
   - 使用通配符：`pgsync "table*"`  
   - 同步特定行：`pgsync products "where store_id = 1"`  
   - 定义表组：在 `.pgsync.yml` 中配置 `groups`，通过 `pgsync group1` 调用。  
4. **高级功能**：  
   - **模式同步**：`--schema-first` 或 `--schema-only` 控制 schema 与数据的同步顺序。  
   - **处理外键**：支持 `--defer-constraints`（推荐）或 `--disable-integrity`（不推荐）。  
   - **敏感数据**：通过 `.pgsync.yml` 中的 `data_rules` 替换敏感字段（如 `email: unique_email`）。  
   - **追加表**：对大表使用 `--append` 模式分批同步。  

**其他支持**  
- **多数据库**：支持多个数据库配置，通过 `.pgsync.yml` 管理。  
- **框架集成**：兼容 Django、Heroku、Laravel、Rails 等框架的数据库迁移需求。  
- **Docker 部署**：提供 Docker 镜像，便于容器化部署。