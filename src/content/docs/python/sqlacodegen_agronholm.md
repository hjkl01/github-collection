
---
title: sqlacodegen
---

### [agronholm sqlacodegen](https://github.com/agronholm/sqlacodegen)  ![GitHub Repo stars](https://img.shields.io/github/stars/agronholm/sqlacodegen?style=social)

sqlacodegen 是一个命令行工具，用于读取现有数据库结构并生成 SQLAlchemy 模型代码。它支持 SQLAlchemy 2.x，能准确自动检测表关系（包括多对多、一对一）及表继承，生成符合 PEP 8 规范的代码。项目内置多种生成器（tables、declarative、dataclasses、sqlmodels），支持 PostgreSQL 扩展类型，并允许用户通过子类化自定义代码生成逻辑。