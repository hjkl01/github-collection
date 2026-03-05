
---
title: sql-tap
---

### [mickamy sql-tap](https://github.com/mickamy/sql-tap)  ![GitHub Repo stars](https://img.shields.io/github/stars/mickamy/sql-tap?style=social)

sql-tap 是一款实时 SQL 流量监控工具，由代理守护进程（sql-tapd）和客户端（TUI/Web）组成。它部署在应用程序与数据库（支持 PostgreSQL、MySQL、TiDB）之间，通过解析数据库协议透明捕获所有查询，无需修改应用代码。核心功能包括：实时查询流展示、事务查看、EXPLAIN/EXPLAIN ANALYZE 分析、结构化过滤（支持按耗时、操作类型等）、N+1 查询自动检测、查询导出及分析视图。用户可通过终端界面或浏览器 Web UI 连接代理进行交互式监控。