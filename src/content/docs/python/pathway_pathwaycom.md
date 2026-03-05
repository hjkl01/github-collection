
---
title: pathway
---

### [pathwaycom pathway](https://github.com/pathwaycom/pathway)  ![GitHub Repo stars](https://img.shields.io/github/stars/pathwaycom/pathway?style=social)

Pathway 是一个基于 Python 的实时数据处理框架，底层由 Rust 引擎驱动，专为流处理、实时分析、LLM 管道和 RAG 应用设计。

**核心特性：**

*   **统一架构**：提供易用 Python API，底层 Rust 引擎支持增量计算、多线程及分布式处理，同一套代码兼容开发、生产、批处理及流数据场景。
*   **数据集成**：内置 Kafka、PostgreSQL 等连接器，通过 Airbyte 支持 300+ 数据源，支持自定义连接器。
*   **处理功能**：支持有/无状态转换（如连接、窗口、排序），可复用任意 Python 函数或库，具备计算状态持久化能力。
*   **LLM 支持**：内置 LLM 工具链（封装器、向量索引等）及 LangChain、LlamaIndex 集成，简化实时 RAG 应用开发。
*   **部署运维**：支持本地、Docker 及 Kubernetes 部署，自动管理数据时序，保障计算一致性（至少一次/确切一次）。