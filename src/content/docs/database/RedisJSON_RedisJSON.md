
---
title: RedisJSON
---

### [RedisJSON RedisJSON](https://github.com/RedisJSON/RedisJSON)  ![GitHub Repo stars](https://img.shields.io/github/stars/RedisJSON/RedisJSON?style=social)

RedisJSON 是 Redis 的一个模块，将 JSON 数据标准作为原生数据类型实现，支持在 Redis 键中存储、更新和获取 JSON 值。其主要功能包括：完整支持 JSON 标准、提供 JSONPath 语法以选择文档元素、以树状二进制结构存储实现快速访问、支持所有 JSON 值类型的原子操作，并可与 RediSearch 配合支持二级索引。注意：自 Redis 8 起，JSON 数据结构已内置于 Redis 核心中，无需单独安装此模块。