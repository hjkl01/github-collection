
---
title: ingestr
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/bruin-data/ingestr?style=social) ](https://github.com/bruin-data/ingestr)
### [bruin-data ingestr](https://github.com/bruin-data/ingestr)

**项目核心内容总结：**  
ingestr 是一个无需编写代码即可将数据从任意源复制到任意目的地的命令行工具。其主要功能包括：  
- **数据迁移**：支持从数据库（如 PostgreSQL、BigQuery、MySQL 等）、平台（如 Google Sheets、Salesforce、Kafka 等）等来源迁移数据到目标地。  
- **增量加载**：支持追加、合并、删除+插入等模式，实现数据同步。  
- **快速安装**：通过 `uv` 工具单命令安装（推荐使用 `uvx ingestr`）。  

**使用方法**：  
运行 `ingestr ingest` 命令，通过参数指定源和目标的连接信息及表名，例如：  
```bash  
ingestr ingest --source-uri 'postgresql://...' --dest-uri 'bigquery://...'  
```  

**特性**：  
- 无需管理后端或编写代码，操作简单；  
- 支持广泛的数据库和平台（部分仅支持单向迁移）；  
- 基于 SQLAlchemy 和 dlt 库构建，依赖其连接能力。