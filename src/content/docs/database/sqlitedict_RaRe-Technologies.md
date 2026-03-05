
---
title: sqlitedict
---

### [RaRe-Technologies sqlitedict](https://github.com/RaRe-Technologies/sqlitedict)  ![GitHub Repo stars](https://img.shields.io/github/stars/RaRe-Technologies/sqlitedict?style=social)

sqlitedict 是一个基于 SQLite 的轻量级 Python 库，用于实现持久化的字典（dict）对象。
核心功能如下：

1.  **字典接口**：提供标准的 Python 字典操作（读写、遍历、计数等）。
2.  **持久化存储**：数据存储在 SQLite 中，支持 GB 级大数据库，不受内存限制。
3.  **多线程支持**：允许同一数据库连接在多线程中使用（请求内部序列化），解决 Python SQLite 的线程限制。
4.  **多表管理**：支持在同一数据库文件中创建和管理多个独立的表（字典）。
5.  **序列化定制**：默认使用 Pickle 序列化值，支持自定义编码器/解码器（如 JSON）及压缩（如 Zlib）。
6.  **易用性**：支持上下文管理器；写入默认需手动 `commit` 或开启 `autocommit` 模式。
7.  **无依赖**：无需额外库，仅依赖 Python 3.7+。
8.  **注意事项**：修改可变对象后需重新赋值回字典并 `commit` 才能生效。