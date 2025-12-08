
---
title: sqlx
---

### [jmoiron sqlx](https://github.com/jmoiron/sqlx)

**项目核心内容总结：**  
sqlx 是 Go 语言的 `database/sql` 标准库扩展，提供更便捷的数据库操作功能。其核心特性包括：  
1. **结构体映射**：自动将查询结果映射到结构体（支持嵌套结构体、字段标签 `db:""`）、map 或切片。  
2. **命名参数支持**：使用 `:name` 或 `:field` 语法进行参数绑定，支持结构体和 map 作为参数源。  
3. **简化查询**：通过 `Get`（单行查询）和 `Select`（多行查询）直接将结果存入结构体或切片。  
4. **批量插入**：支持通过 `[]map[string]interface{}` 或结构体切片进行批量插入。  
5. **兼容性**：兼容最新两个 Go 版本，使用 Go 模块管理版本，重大变更会升级主版本号。  

**使用方法**：  
- 安装：`go get github.com/jmoiron/sqlx`。  
- 连接数据库：`sqlx.Connect("driver", "dsn")`。  
- 插入数据：使用 `Exec`、`NamedExec`（支持结构体/Map 参数）。  
- 查询数据：通过 `Select`（多行）或 `Get`（单行）直接映射到结构体，或使用 `Queryx` 配合 `StructScan` 手动处理结果。  
- 处理 NULL 值：结构体中使用 `sql.NullString` 等类型。  

**注意事项**：  
- 查询时避免列名冲突（如使用 `AS` 显式命名列）。  
- 使用 `BindDriver` 可自定义驱动绑定规则（如非默认的绑定变量语法）。