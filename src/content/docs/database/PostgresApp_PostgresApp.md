
---
title: PostgresApp
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/PostgresApp/PostgresApp?style=social) ](https://github.com/PostgresApp/PostgresApp)
### [PostgresApp PostgresApp](https://github.com/PostgresApp/PostgresApp)

**核心内容总结：**

Postgres.app 是一款专为 Mac 设计的 PostgreSQL 图形化管理工具，提供以下功能和特性：

1. **功能与使用方法**  
   - 一键集成 PostgreSQL 服务及常用扩展（如 PostGIS、pgrouting、pgvector 等），无需手动配置。  
   - 提供图形化界面启动/停止服务器，支持同时运行多个 PostgreSQL 版本。  
   - 下载地址为官网（[postgresapp.com](http://postgresapp.com/)），旧版本和预发布版可通过 GitHub 发布页获取。  
   - 文档可通过官网或应用内“打开文档”菜单访问。

2. **主要特性**  
   - 包含 PostgreSQL 二进制文件、命令行工具（如 `psql`、`pg_dump` 等）及扩展（如 PostGIS、GDAL 等）。  
   - 支持通过命令行初始化数据库集群、创建用户和数据库。  
   - 服务器以当前用户权限运行，而非独立系统用户。

3. **构建与依赖**  
   - **GUI 构建**：需 Xcode 11 及以上，无需重新编译 PostgreSQL 二进制文件，直接使用应用内已安装的版本。  
   - **二进制文件构建**：需根据 PostgreSQL 版本选择对应 macOS 和 Xcode 版本（如 PostgreSQL 17-18 需 macOS 14 和 Xcode 15.3）。  
   - 依赖项包括 Python（版本因 PostgreSQL 版本而异）、MacPorts 或 Homebrew 安装的 autoconf、automake、pkgconfig 等工具。

4. **调试支持**  
   - 使用 `pldebugger` 调试 pl/pgsql 代码需修改 `postgresql.conf` 配置文件并加载扩展，需配合 PgAdmin 4 等支持调试的客户端。