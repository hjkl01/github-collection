
---
title: pgweb
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/sosedoff/pgweb?style=social) ](https://github.com/sosedoff/pgweb)
### [sosedoff pgweb](https://github.com/sosedoff/pgweb)

**项目核心内容总结：**

**功能**  
pgweb 是一个基于 Web 的 PostgreSQL 数据库管理工具，支持跨平台（Mac/Linux/Windows），提供数据库连接、SQL 查询执行、数据导出（CSV/JSON/XML）、查询历史记录、服务器书签等功能，无需安装额外依赖。

**主要特性**  
- 跨平台支持（64位系统）  
- 单文件安装，无依赖  
- 支持 PostgreSQL 9.1 及以上版本  
- 支持 SSH 隧道连接  
- 多数据库会话管理  
- 数据导出与查询分析  
- 提供在线演示（[https://pgweb-demo.fly.dev](https://pgweb-demo.fly.dev)）  

**使用方法**  
1. **启动服务**：直接运行 `pgweb`  
2. **连接参数**：通过命令行指定 `--host`、`--user`、`--db` 等参数，或使用 URL 格式：  
   ```bash  
   pgweb --url "postgres://user:password@host:port/database?sslmode=mode"  
   ```  
3. **多会话模式**：启动时添加 `--sessions` 参数或设置环境变量 `PGWEB_SESSIONS=1`  

**安装方式**  
- 下载预编译的二进制文件（支持多平台）  
- 参考 Wiki 获取更多安装选项（如 Docker 部署）