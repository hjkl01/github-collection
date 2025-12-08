
---
title: pgloader
---

### [dimitri pgloader](https://github.com/dimitri/pgloader)

pgloader 是一个用于 PostgreSQL 的数据加载工具，核心功能是通过 `COPY` 命令实现高效数据迁移。其主要特性包括：  
1. **事务处理**：在加载过程中，若遇到错误数据，会将其隔离记录到单独文件中，同时继续加载有效数据，避免因单条错误中断整个操作。  
2. **数据格式转换**：支持自动处理特殊格式（如将 MySQL 的 `0000-00-00` 转换为 PostgreSQL 的 `NULL`）。  
3. **多源支持**：可迁移 SQLite、MySQL 等数据库数据至 PostgreSQL，支持并行加载。  

**使用方法**：  
- 命令行直接调用，如 `pgloader sqlite.db postgresql:///newdb`。  
- 通过配置文件定义加载规则，支持参数化设置（如编码、字段映射、转换规则）。  
- 提供 `--help` 查看参数，`--version` 查看版本，`--dry-run` 测试连接等选项。  

**安装**：Debian 系统可直接使用 `apt-get install pgloader`，Docker 用户可通过镜像运行。