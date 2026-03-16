### [RaRe-Technologies sqlitedict](https://github.com/RaRe-Technologies/sqlitedict)  ![GitHub Repo stars](https://img.shields.io/github/stars/RaRe-Technologies/sqlitedict?style=social)

sqlitedict 是一个基于 Python sqlite3 的轻量级持久化字典库，提供类 dict 接口。核心功能如下：
* **持久化存储**：支持任意可序列化对象（默认 Pickle），处理大容量数据，不受内存限制。
* **灵活序列化**：支持自定义值编码/解码（如 JSON、压缩）及键编码。
* **多表支持**：同一数据库文件可存储多个表（字典）。
* **多线程访问**：支持多线程操作同一连接（内部串行化），解决 Python sqlite3 线程限制。
* **便捷操作**：支持上下文管理器，提供显式或自动提交，兼容 items()、keys() 等标准方法。