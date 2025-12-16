
---
title: asyncpg
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/MagicStack/asyncpg?style=social) ](https://github.com/MagicStack/asyncpg)
### [MagicStack asyncpg](https://github.com/MagicStack/asyncpg)

**asyncpg** 是一个专为 PostgreSQL 和 Python/asyncio 设计的高性能异步数据库客户端库，支持原生 PostgreSQL 协议，提供高效的数据交互能力。  

**核心功能**  
- 支持异步查询、预处理语句、可滚动游标、部分结果迭代。  
- 自动编码/解码复合类型、数组等数据结构，支持自定义数据类型。  
- 兼容 PostgreSQL 9.5 至 18 版本，性能测试显示平均比 psycopg3 快 5 倍。  

**使用方法**  
通过 pip 安装（`pip install asyncpg`），使用 `async/await` 连接数据库并执行查询，例如：  
```python  
async def run():  
    conn = await asyncpg.connect(...)  
    values = await conn.fetch('SELECT * FROM mytable WHERE id = $1', 10)  
```  

**安装依赖**  
- 默认无依赖，需 GSSAPI/SSPI 认证时安装 `asyncpg[gssauth]`。  

**许可证**  
采用 Apache 2.0 协议开源。