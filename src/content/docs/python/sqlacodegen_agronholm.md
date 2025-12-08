
---
title: sqlacodegen
---

### [agronholm sqlacodegen](https://github.com/agronholm/sqlacodegen)

**项目核心内容总结**：

sqlacodegen 是一个工具，用于根据现有数据库结构自动生成 SQLAlchemy 模型代码，支持声明式风格。其主要功能包括：

1. **功能**  
   - 支持 SQLAlchemy 2.x  
   - 生成符合 PEP8 规范的代码，接近手写风格  
   - 自动检测数据库关系（如多对多、一对一）、继承结构  
   - 提供多种代码生成器（如 `declarative`、`dataclasses`、`sqlmodels`）  
   - 高测试覆盖率  

2. **使用方法**  
   - 安装：`pip install sqlacodegen`，可选安装扩展（如 `sqlacodegen[citext]`）  
   - 命令行使用：指定数据库 URL 和生成器类型（如 `sqlacodegen postgresql:///some_local_db`）  
   - 支持自定义选项（如 `--options noconstraints` 忽略约束）  

3. **特性**  
   - 支持多种数据库类型（MySQL、PostgreSQL、Oracle 等）  
   - 生成器可配置命名规则（如使用 `inflect` 库将表名转为单数形式）  
   - 自动识别关联表并生成对应模型  
   - 支持自定义代码生成逻辑（通过扩展入口点实现）