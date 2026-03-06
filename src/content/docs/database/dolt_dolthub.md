
---
title: dolt
---

### [dolthub dolt](https://github.com/dolthub/dolt)  ![GitHub Repo stars](https://img.shields.io/github/stars/dolthub/dolt?style=social)

Dolt 是一款支持版本控制的 SQL 数据库，被称为“数据的 Git"。它兼容 MySQL 协议，允许用户像管理 Git 仓库一样管理数据库表。

主要功能：
1. **版本控制**：支持表的 fork、clone、branch、merge、push、pull 等操作，以及 commit 历史管理。
2. **操作界面**：提供类 Git 的命令行工具（CLI）及基于 SQL 的系统表、函数和存储过程。
3. **数据回溯**：支持时间旅行查询、单元格级变更追踪、差异对比（diff）及审计功能。
4. **容错机制**：支持撤销更改、回退特定版本、恢复误删表或数据库。
5. **扩展支持**：支持 Linux、Mac、Windows、Docker 等部署，可同步现有 MySQL 数据，并提供 PostgreSQL 兼容版本（Doltgres）及云端托管服务。