
---
title: fake2db
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/emirozer/fake2db?style=social) ](https://github.com/emirozer/fake2db)
### [emirozer fake2db](https://github.com/emirozer/fake2db)

**项目功能**  
fake2db 是一个用于生成假但有效数据库数据的工具，支持 SQLite、MySQL、PostgreSQL、MongoDB、Redis、CouchDB 等数据库，适用于测试场景。  

**使用方法**  
通过命令行参数指定生成数据量（`--rows`）、数据库类型（`--db`）及连接信息（如 `--host`、`--port`、`--username`、`--password`），可选参数包括数据库名称（`--name`）、数据本地化（`--locale`）和随机种子（`--seed`）。例如：  
`fake2db --rows 200 --db sqlite`  

**主要特性**  
1. 支持多种数据库类型，可自定义生成表结构（`--custom` 参数指定字段）。  
2. 数据本地化（如 `--locale=cs_CZ`）和随机种子（`--seed`）确保数据一致性。  
3. 可连接远程数据库（需指定主机、端口、用户名、密码）。  
4. 提供 FoundationDB SQL Layer 的兼容支持（通过 PostgreSQL 模式）。