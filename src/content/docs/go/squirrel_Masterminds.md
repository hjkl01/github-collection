
---
title: squirrel
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/Masterminds/squirrel?style=social) ](https://github.com/Masterminds/squirrel)
### [Masterminds squirrel](https://github.com/Masterminds/squirrel)

**项目核心内容总结：**

**功能**  
Squirrel 是一个用于 Go 语言的 SQL 查询生成器，通过可组合的语法构建 SQL 语句，不依赖 ORM。支持 SELECT、INSERT、UPDATE 等操作，可直接执行查询或生成 SQL 字符串。

**使用方法**  
1. 导入包：`import "github.com/Masterminds/squirrel"`  
2. 构建查询：通过链式方法（如 `Select().From().Where()`）组合查询条件。  
3. 生成 SQL：调用 `ToSql()` 获取 SQL 字符串及参数。  
4. 执行查询：通过 `RunWith(db).Query()` 直接执行数据库操作。  

**主要特性**  
- 支持复杂查询构建，如 JOIN、WHERE 条件、IN 查询（通过 `sq.Eq` 处理多值）。  
- 可自定义占位符格式（如 PostgreSQL 的 `$1,$2`）。  
- 提供 `StmtCache` 缓存预处理语句，优化性能。  
- 与 PostgreSQL 兼容，支持 `RETURNING` 子句等语法。  
- 支持动态条件拼接（如通过 `if` 判断添加 `Where` 条件）。  

**注意事项**  
- 不处理 `[]uint8` 类型的 IN 查询（需用 `[]byte` 代替）。  
- 复合键 IN 查询需用 `sq.Or` 模拟 `(col1, col2) IN ((...))` 效果。