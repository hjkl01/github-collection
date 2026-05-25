### [lynxdb](https://github.com/lynxbase/lynxdb) ![GitHub Repo stars](https://img.shields.io/github/stars/lynxbase/lynxdb?style=social)

LynxDB 是一个**单二进制、零依赖**的日志分析数据库，支持两种使用方式：  
1) 像 `grep` 一样直接从管道/文件查询（无需服务、无需配置）；  
2) 作为持久化服务运行并进行日志摄取与检索。

项目核心能力包括：  
- **Lynx Flow 查询语言**（管道式左到右处理），支持 `parse`、`let`、`where`、`group`、`order by`、`join`、CTE 等，并提供**部分 SPL2 兼容**。  
- **全文检索与高效索引**：FST 倒排索引、roaring bitmaps、bloom filter 跳段。  
- **列式存储引擎**：自定义 `.lsg` 格式，结合时间戳压缩、字典编码、Gorilla XOR、LZ4 等优化。  
- **物化视图**：支持预聚合与自动查询改写，查询可显著加速（最高约 400x）。  
- **集群与对象存储**：可通过 `--cluster.seeds` 分布式部署，支持 S3 共享存储。  
- **多协议接入**：兼容 Elasticsearch `_bulk`、OpenTelemetry OTLP、Splunk HEC。  
- **Sigma 规则支持**：可运行 rsigma 转换后的 SPL2 查询。

同时提供完整 CLI 工具集（query、tail、ingest、shell、watch、diff、explain、mv、status、bench、demo 等），并强调**默认零配置**、轻量资源占用与快速上手。当前项目处于活跃开发阶段，API/存储格式/查询行为可能变更。