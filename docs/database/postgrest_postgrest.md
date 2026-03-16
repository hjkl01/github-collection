### [postgrest postgrest](https://github.com/postgrest/postgrest)  ![GitHub Repo stars](https://img.shields.io/github/stars/postgrest/postgrest?style=social)

PostgREST 是一个能从现有 PostgreSQL 数据库自动生成 RESTful API 的服务，提供比手写代码更标准、性能更快且易于扩展的解决方案。主要功能特性包括：基于 Haskell 的高性能实现，将 JSON 序列化、数据验证及授权等计算委托给数据库执行；通过 JWT 处理认证并依据数据库角色进行授权；利用数据库 Schema 实现 API 版本控制；自动生成符合 OpenAPI 标准的可交互文档；依靠数据库声明式约束保障数据完整性及请求幂等性。