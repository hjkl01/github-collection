
---
title: sqlitedict
---

### [RaRe-Technologies sqlitedict](https://github.com/RaRe-Technologies/sqlitedict)

**项目核心内容总结：**

**功能**  
`sqlitedict` 是一个基于 SQLite 的持久化字典工具，提供类似 Python 字典的接口，支持多线程访问、自定义序列化及多表存储。数据以 SQLite 数据库文件形式保存，适用于需要持久化存储复杂对象的场景。

**使用方法**  
1. **安装**：通过 `pip install -U sqlitedict` 安装。  
2. **基本操作**：  
   - 写入：创建 `SqliteDict` 实例，通过 `db[key] = value` 存储数据，需手动调用 `commit()` 提交（或启用 `autocommit=True`）。  
   - 读取：通过 `db[key]` 或 `items()/keys()/values()` 遍历数据。  
   - 关闭：使用 `db.close()` 或上下文管理器 `with SqliteDict(...) as db:` 自动关闭。  
3. **多表存储**：通过 `tablename` 参数指定表名，同一数据库文件可存储多个表。  
4. **自定义序列化**：通过 `encode`/`decode` 参数替换默认的 `pickle`（如使用 `json` 或压缩）。  
5. **键编码**：支持非字符串键，需传入自定义 `encode_key`/`decode_key` 函数。

**主要特性**  
- 支持任意可序列化对象（默认使用 `pickle` 最高协议）。  
- 多线程安全（解决 SQLite 在 Python 中的线程限制）。  
- 自定义编解码器，支持 JSON、压缩等扩展。  
- 高效处理大数据库（SQLite 本身内存优化）。  
- 提供 `len()`、`items()` 等字典接口，但注意 `len()` 需扫描全表。  
- **注意事项**：修改字典值需重新赋值（如 `db[key] = new_value`）才能持久化；未提交数据会丢失。