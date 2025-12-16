
---
title: migrate
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/golang-migrate/migrate?style=social) ](https://github.com/golang-migrate/migrate)
### [golang-migrate migrate](https://github.com/golang-migrate/migrate)

**核心内容总结：**  
该项目是一个用Go编写的数据库迁移工具，支持通过CLI或作为库集成到Go项目中。  

**功能：**  
- 支持多种数据库（如PostgreSQL、MySQL、SQLite、MongoDB等）和迁移源（如文件系统、GitHub、S3等）。  
- 提供命令行工具执行迁移操作（如`up`、`down`），支持通过Docker运行。  
- 作为库使用时，支持线程安全、优雅关闭、自定义日志和低内存开销。  

**使用方法：**  
1. **CLI方式**：通过命令指定数据库连接和迁移源，例如：  
   ```bash  
   migrate -source file://path/to/migrations -database postgres://localhost:5432/database up 2  
   ```  
2. **Go库集成**：导入库并初始化迁移实例，例如：  
   ```go  
   import (  
       "github.com/golang-migrate/migrate/v4"  
       _ "github.com/golang-migrate/migrate/v4/database/postgres"  
   )  
   m, _ := migrate.New("source", "database")  
   m.Up()  
   ```  

**主要特性：**  
- 数据库驱动轻量化，逻辑由迁移工具统一管理。  
- 数据库连接URL需遵循特定编码规范（如特殊字符需URL编码）。  
- CLI支持优雅处理中断信号（SIGINT）。  
- Go库支持版本控制（v3/v4）、多数据库实例和自定义配置。  
- 支持从多种远程源（GitHub、S3等）读取迁移文件。  

**版本支持：**  
- 主分支（master）和v4为当前稳定版本，v3已停止维护。