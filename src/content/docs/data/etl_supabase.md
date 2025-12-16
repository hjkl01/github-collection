
---
title: etl
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/supabase/etl?style=social) ](https://github.com/supabase/etl)
### [supabase etl](https://github.com/supabase/etl)

**项目核心内容总结**  

ETL 是 Supabase 开发的 Rust 框架，用于构建基于 PostgreSQL 的高性能实时数据复制应用。它基于 PostgreSQL 逻辑复制协议，提供类型安全的 Rust API，支持将数据库变更实时同步到自定义目的地。  

**主要特性**  
- 实时复制：支持从 PostgreSQL 流式传输数据变更到任意目的地。  
- 高性能：支持配置化批量处理和并行化以提升吞吐量。  
- 容错性：内置错误处理和重试机制。  
- 可扩展：支持自定义目的地和状态/模式存储。  
- 生产级支持：官方提供 BigQuery 和 Apache Iceberg 的同步能力。  
- 类型安全：编译时类型检查保障代码可靠性。  

**使用方法**  
1. 通过 Git 安装（暂未发布到 crates.io）：  
   ```toml  
   etl = { git = "https://github.com/supabase/etl" }  
   ```  
2. 配置 PostgreSQL 连接、存储（如内存）和目的地（如 BigQuery），定义流水线参数（如批次大小、重试策略）。  
3. 启动流水线并运行。  

**依赖与要求**  
- PostgreSQL 14-17 版本，推荐 15+ 以使用高级发布功能（如列级过滤、模式级同步）。  
- 通过 `etl-destinations` crate 启用特定目的地（如 BigQuery）。  

**开发与贡献**  
- 项目优先保障核心稳定性与易用性，暂不接受新自定义目的地提案（除非社区有显著需求）。