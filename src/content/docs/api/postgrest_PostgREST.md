
---
title: postgrest
---

### [PostgREST postgrest](https://github.com/PostgREST/postgrest)  ![GitHub Repo stars](https://img.shields.io/github/stars/PostgREST/postgrest?style=social)

PostgREST 是一款基于现有 PostgreSQL 数据库自动生成 RESTful API 的工具。相比手写 API，它更标准、更简洁且性能更优。核心功能包括：通过 Haskell 实现高性能高并发，将计算任务（如序列化、验证、授权）委托给数据库；支持 JWT 认证并将权限控制委托给数据库角色；利用数据库 Schema 实现 API 版本控制；基于 OpenAPI 标准自动生成文档；通过强制数据库约束保障数据完整性，防止数据被应用层破坏。