### [RedisJSON RedisJSON](https://github.com/RedisJSON/RedisJSON)  ![GitHub Repo stars](https://img.shields.io/github/stars/RedisJSON/RedisJSON?style=social)

RedisJSON 是 Redis 模块，将 JSON 标准作为原生数据类型实现，支持对 Redis 键中的 JSON 文档进行存储、更新和获取。主要功能包括：完整支持 JSON 标准、使用 JSONPath 语法选择元素、以二进制树结构存储以实现快速子元素访问、支持所有 JSON 值类型的类型化原子操作，以及配合 RediSearch 支持二级索引。注意：自 Redis 8 起 JSON 已集成至 Redis 核心，不再单独发布独立版本。