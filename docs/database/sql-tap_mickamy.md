### [mickamy sql-tap](https://github.com/mickamy/sql-tap)  ![GitHub Repo stars](https://img.shields.io/github/stars/mickamy/sql-tap?style=social)

sql-tap 是一款实时 SQL 流量查看工具，由代理守护进程（sql-tapd）和 TUI/Web 客户端组成。它部署在应用程序与数据库（PostgreSQL、MySQL 或 TiDB）之间，无需修改应用代码即可透明捕获所有 SQL 查询并实时展示。核心功能涵盖：交互式终端与网页查看、查询与事务检查、执行 EXPLAIN/ANALYZE 分析、N+1 查询模式自动检测、多维度过滤（如耗时、操作类型、错误）以及查询导出。