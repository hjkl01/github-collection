
---
title: sqlite-web
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/coleifer/sqlite-web?style=social) ](https://github.com/coleifer/sqlite-web)
### [coleifer sqlite-web](https://github.com/coleifer/sqlite-web)

**核心内容总结：**  
`sqlite-web` 是一个基于 Python 的 Web 工具，用于浏览和管理 SQLite 数据库。  

**功能：**  
- 支持查看、编辑现有 SQLite 数据库或新建数据库；  
- 可添加/删除表、列、索引，支持旧版 SQLite 的列操作；  
- 支持数据导出（JSON/CSV）和导入（CSV/JSON）；  
- 提供数据浏览、增删改查操作，支持 SQL 查询执行及结果导出；  
- 支持分页显示、密码保护、只读模式等。  

**使用方法：**  
1. **本地安装**：通过 `pip install sqlite-web` 安装后，运行 `sqlite_web /path/to/database.db` 启动服务，访问 http://localhost:8080 查看数据库。  
2. **Docker 部署**：使用 Docker 命令挂载数据库路径并指定数据库文件名，通过 `ghcr.io/coleifer/sqlite-web` 镜像运行。  

**主要特性：**  
- 提供数据库结构、数据内容、查询结果等多标签页浏览；  
- 支持自定义端口、日志路径、SSL 配置等命令行参数；  
- 可通过 Docker 快速部署，兼容多种 SQLite 操作需求。