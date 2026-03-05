
---
title: sqlacodegen
---

### [agronholm sqlacodegen](https://github.com/agronholm/sqlacodegen)  ![GitHub Repo stars](https://img.shields.io/github/stars/agronholm/sqlacodegen?style=social)

sqlacodegen 是一个命令行工具，用于读取现有数据库结构并自动生成相应的 SQLAlchemy 模型代码。

核心功能：
* 支持 SQLAlchemy 2.x，生成符合 PEP 8 规范的高质量代码。
* 提供多种代码生成器：`declarative`（默认，生成 ORM 类）、`tables`（生成 Table 对象）、`dataclasses` 和 `sqlmodels`。
* 准确检测数据库关系（多对多、一对一、多对一）及联合表继承。
* 支持多种数据库及扩展类型（如 PostgreSQL 的 CITEXT、GEOMETRY、PGVECTOR 等）。
* 允许通过命令行选项自定义生成逻辑（如忽略约束、索引、枚举处理等），并支持通过子类化扩展自定义生成器。