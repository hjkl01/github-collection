
---
title: pgloader
---

### [dimitri pgloader](https://github.com/dimitri/pgloader)  ![GitHub Repo stars](https://img.shields.io/github/stars/dimitri/pgloader?style=social)

PGLoader 是一款基于 COPY 命令的 PostgreSQL 数据加载工具。其核心优势在于容错机制：遇到错误数据时不中断任务，而是将错误数据单独记录并继续加载有效数据。它支持数据格式转换（如日期处理）、从 MySQL 或 SQLite 等源进行全量迁移（含架构定义），支持并行加载，并提供命令行和配置文件等多种使用方式。