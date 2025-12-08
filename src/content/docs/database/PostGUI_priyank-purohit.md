
---
title: PostGUI
---

### [priyank-purohit PostGUI](https://github.com/priyank-purohit/PostGUI)

**项目核心内容总结：**

**功能**：PostGUI 是一个基于 React 的 Web 应用，通过 PostgREST 工具实现对 PostgreSQL 数据库的查询与共享。支持数据库结构展示、可视化 SQL 查询构建、用户权限控制，适用于本地或互联网数据共享场景。

**主要特性**：
1. **数据库适配**：自动适配任意 PostgreSQL 数据库结构，支持读写操作（需主键定义）。
2. **多数据库管理**：通过配置文件支持多个数据库共享。
3. **交互功能**：提供搜索、查询构建器（无需 SQL 知识）、数据表格展示、CSV/JSON/XML 下载、内容编辑记录。
4. **安全控制**：集成基础认证系统（读/写/管理员权限），支持 HTTPS 部署。

**使用方法**：
1. **环境准备**：安装 Node.js、PostgreSQL、PostgREST。
2. **数据库设置**：导入示例数据库或自定义数据，配置主键、视图、索引。
3. **配置 PostgREST**：创建 `db.conf` 文件，设置数据库连接参数。
4. **配置 PostGUI**：修改 `/src/data/config.json` 中的 PostgREST 地址和数据库标题。
5. **运行应用**：执行 `npm start` 启动 Web 界面。

**部署注意事项**：启用 HTTPS、优化 PostgREST 安全配置、完善用户认证系统。