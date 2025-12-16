
---
title: Daft
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/Eventual-Inc/Daft?style=social) ](https://github.com/Eventual-Inc/Daft)
### [Eventual-Inc Daft](https://github.com/Eventual-Inc/Daft)

**项目核心内容总结：**  
Daft 是一个高性能数据引擎，专为 AI 和多模态工作负载设计，支持图像、音频、视频及结构化数据的统一处理。其主要特性包括：  
- **多模态处理**：在单一框架中处理图像、音频、视频、嵌入向量及结构化数据。  
- **内置 AI 操作**：支持大规模运行 LLM 提示、生成嵌入向量及数据分类（兼容 OpenAI、Transformers 等模型）。  
- **性能与扩展性**：基于 Python 与 Rust 构建，提供本地及分布式集群（Ray、Kubernetes、Daft Cloud）无缝扩展能力。  
- **数据连接**：支持 S3、GCS、Iceberg、Delta Lake 等多源数据接入。  
- **可靠性**：智能内存管理与默认配置减少调优复杂度。  

**使用方法**：  
通过 `pip install daft` 安装（需 Python 3.10+），详细步骤见官方文档。快速入门包含加载电商数据集、处理图像及运行 AI 推理的示例。  

**其他信息**：  
- 提供示例、用户指南及 API 文档。  
- 基准测试对比其他框架（如 Pandas、Polars、PySpark 等）。  
- 默认收集非标识性使用数据，可通过 `DO_NOT_TRACK=true` 禁用。  
- 采用 Apache 2.0 许可证。