
---
title: tinydb
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/msiemens/tinydb?style=social) ](https://github.com/msiemens/tinydb)
### [msiemens tinydb](https://github.com/msiemens/tinydb)

**核心内容总结：**  
TinyDB 是一个轻量级的文档型数据库，专为小型应用设计，无需依赖外部数据库服务器或 SQL 数据库。其核心功能包括：  
- **功能**：支持存储和查询任意文档（以字典形式表示），提供类似 MongoDB 的查询语法（如 `==`、`>`、`<`、`&`、`|` 等操作符），支持表格管理和中间件扩展。  
- **使用方法**：通过 `TinyDB` 初始化数据库，使用 `insert` 存储数据，通过 `Query` 对象构建查询条件（如 `User.name == 'John'`），支持复杂查询组合与字段变换（如 `map`）。  
- **特性**：  
  - **轻量**：代码量约 1800 行，100% 测试覆盖率。  
  - **纯 Python 实现**：无需安装外部依赖或数据库服务器。  
  - **兼容性**：支持 Python 3.8–3.13 及 PyPy3。  
  - **可扩展**：可通过自定义存储或中间件（如缓存）扩展功能。  
- **状态**：项目处于维护模式，不计划新增重大功能，但会修复 Bug 并接受社区贡献。