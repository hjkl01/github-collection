
---
title: lazysql
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/jorgerojas26/lazysql?style=social) ](https://github.com/jorgerojas26/lazysql)
### [jorgerojas26 lazysql](https://github.com/jorgerojas26/lazysql)

**项目核心内容总结：**  

**功能**：LAZYSQL 是一个基于终端的数据库管理工具，支持 PostgreSQL、MySQL、SQLite 和 MSSQL（未来将支持 NoSQL）。提供数据库连接、SQL 执行、表结构管理（如增删改列、索引）、自定义命令（如 SSH 隧道配置）等功能。  

**使用方法**：  
1. **安装**：通过 Homebrew 安装或从源码编译。  
2. **配置**：编辑配置文件，定义数据库连接信息（URL、认证）、自定义命令（如 `ssh` 隧道）及变量替换规则。  
3. **操作**：运行 `lazysql` 命令，通过终端界面选择数据库连接，使用快捷键（如 `CTRL+e` 打开 SQL 编辑器、`c` 编辑单元格）进行数据操作。  

**主要特性**：  
- 支持多种关系型数据库及自定义命令链。  
- 提供终端用户界面（TUI）操作表结构（如新增/删除行、排序、刷新数据）。  
- 支持剪贴板复制（需依赖系统工具）。  
- 可自定义快捷键及键绑定。  
- 配置文件支持变量替换（如动态端口分配）。  

**开发计划**：优化 NoSQL 支持、增强表结构操作功能、改进用户交互体验。