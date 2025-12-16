
---
title: etl
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/supabase/etl?style=social) ](https://github.com/supabase/etl)
### [supabase etl](https://github.com/supabase/etl)

**项目核心内容总结：**

ETL 是 Supabase 开发的 Rust 框架，用于构建基于 PostgreSQL 的实时数据复制应用。其核心功能是通过 PostgreSQL 逻辑复制技术，将数据库变更实时流式传输至自定义目的地（如 BigQuery、Apache Iceberg 等），并提供类型安全的 Rust API。

**主要特性：**
- 实时复制：支持实时捕获 PostgreSQL 数据变更并传输至目标系统。
- 高性能：支持批量配置和并行处理以提升吞吐量。
- 容错性：内置错误处理和重试机制。
- 可扩展：允许用户自定义目的地及状态/模式存储。
- 生产级支持：官方提供 BigQuery 和 Iceberg 的完整复制能力。
- 类型安全：Rust 原生 API 提供编译时类型校验。

**使用方法：**
1. 通过 Git 安装依赖：`etl = { git = "https://github.com/supabase/etl" }`。
2. 配置 PostgreSQL 连接参数（如主机、端口、数据库名等）。
3. 选择目的地（如内存测试用 `MemoryDestination`）。
4. 定义管道配置（包括批次大小、重试策略等）。
5. 调用 `Pipeline::new()` 启动数据复制流程。

**要求：**
- PostgreSQL 14-17 版本（推荐 15+ 以使用高级发布功能）。
- 需通过 `etl-destinations` 单独启用 BigQuery 等目的地支持。