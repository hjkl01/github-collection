
---
title: ibis
---

### [ibis-project ibis](https://github.com/ibis-project/ibis)

**Ibis 核心内容总结：**

**项目功能**  
Ibis 是一个可移植的 Python 数据框库，提供统一的 API 用于数据处理，支持本地（如 DuckDB）和远程（如 SQL 数据库）执行，兼容近 20 种后端（如 Spark、BigQuery、PostgreSQL 等）。  

**主要特性**  
1. **多后端支持**：同一代码可在不同后端（如 DuckDB、Polars、SQL 数据库）间无缝切换，无需修改逻辑。  
2. **Python 与 SQL 结合**：支持将 Python 表达式编译为 SQL，或直接混合使用 SQL 语句。  
3. **交互式探索**：提供交互模式，便于数据探索与分析。  
4. **性能优化**：默认使用 DuckDB 实现快速本地计算，支持延迟执行与大规模数据处理。  
5. **部署灵活性**：通过修改单行代码（如 `ibis.set_backend("bigquery")`）即可切换执行环境。  

**使用方法**  
1. 安装：`pip install 'ibis-framework[duckdb,examples]'`。  
2. 示例代码：  
   ```python  
   import ibis  
   ibis.options.interactive = True  
   t = ibis.examples.penguins.fetch()  # 加载示例数据  
   g = t.group_by("species").agg(count=t.count())  # 分组统计  
   ```  
3. 切换后端：  
   ```python  
   ibis.set_backend("duckdb")  # 或 "pandas", "bigquery" 等  
   con = ibis.duckdb.connect()  # 创建连接对象  
   t = con.table("penguins")    # 读取表数据  
   ```