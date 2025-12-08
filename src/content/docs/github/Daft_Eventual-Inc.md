
---
title: Daft
---

### [Eventual-Inc Daft](https://github.com/Eventual-Inc/Daft)

**Daft 项目核心内容总结：**

**项目功能**  
Daft 是一个高性能数据引擎，支持处理图像、音频、视频、结构化数据及多模态数据，适用于大规模 AI 和多模态工作负载。内置 AI 操作（如 LLM 提示、嵌入生成、分类），兼容 OpenAI、Transformers 及自定义模型。支持本地与分布式集群（Ray、Kubernetes、Daft Cloud）无缝扩展，可连接 S3、GCS、Iceberg、Delta Lake 等数据源。

**使用方法**  
通过 `pip install daft` 安装（需 Python 3.10+），详细安装步骤见官方文档。快速入门提供加载电商数据集、处理图像及运行 AI 推理的示例。

**主要特性**  
- **多模态处理**：统一处理图像、音频、视频及结构化数据。  
- **AI 集成**：支持大规模 AI 操作，兼容主流模型框架。  
- **性能**：Python 接口 + Rust 内核，兼顾开发效率与运行速度。  
- **扩展性**：从本地单机无缝扩展至分布式集群。  
- **连接性**：支持主流云存储与数据湖（S3、GCS、Delta Lake 等）。  
- **可靠性**：智能内存管理与默认配置减少调优复杂度。  

**其他**  
提供基准测试数据、贡献指南及遥测数据收集选项（可关闭）。对比其他数据处理工具（如 Pandas、Polars），Daft 在多模态、分布式、向量化执行等方面具有优势。许可证为 Apache 2.0。