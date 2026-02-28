
---
title: sql-tap
---

### [mickamy sql-tap](https://github.com/mickamy/sql-tap)  ![GitHub Repo stars](https://img.shields.io/github/stars/mickamy/sql-tap?style=social)

sql-tap 是一款实时 SQL 流量查看工具，由代理守护进程（sql-tapd）和客户端（TUI/Web）组成，透明拦截应用程序与数据库（PostgreSQL、MySQL、TiDB）间的 SQL 流量，无需修改应用代码。

**主要特性**：
- **实时可视化**：支持终端 UI（TUI）和 Web 界面，实时展示查询、事务及执行状态。
- **查询分析**：支持 EXPLAIN/EXPLAIN ANALYZE（需配置 DATABASE_URL 环境变量），可编辑后重新执行分析。
- **N+1 检测**：自动检测相同模板在短时间窗口内的重复 SELECT 查询，支持告警与高亮。
- **高级过滤**：支持按执行时间、操作类型（SELECT/INSERT 等）及文本内容组合筛选。
- **便捷操作**：支持查询复制（含参数）、导出为 JSON/Markdown、快捷键导航。

**使用方法**：
1. **安装**：支持 Homebrew、Go、源码编译或 Docker 部署。
2. **启动代理**：运行 `sql-tapd` 并指定驱动、监听地址及上游数据库地址（例如代理 PostgreSQL 的 5432 端口）。
3. **配置应用**：将应用程序的数据库连接指向代理端口。
4. **启动客户端**：运行 `sql-tap` 连接代理查看 TUI，或启用 `--http` 参数通过浏览器访问 Web UI。

**注意**：搜索/过滤模式下，终端按键输入可能存在解析限制（如无法输入 `[A` 等字符）。