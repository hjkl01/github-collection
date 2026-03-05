
---
title: pgloader
---

### [dimitri pgloader](https://github.com/dimitri/pgloader)  ![GitHub Repo stars](https://img.shields.io/github/stars/dimitri/pgloader?style=social)

PGLoader 是一款基于 COPY 命令的 PostgreSQL 数据加载工具。其核心优势在于容错机制，遇到错误数据行时不会中断任务，而是将错误数据单独记录并继续加载有效数据。此外，它支持数据格式转换（如将无效日期转换为 NULL）、从 MySQL/SQLite 等多源向 PostgreSQL 迁移数据，并支持命令行或配置文件操作。