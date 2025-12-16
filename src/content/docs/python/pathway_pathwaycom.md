
---
title: pathway
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/pathwaycom/pathway?style=social) ](https://github.com/pathwaycom/pathway)
### [pathwaycom pathway](https://github.com/pathwaycom/pathway)

**项目功能**：Pathway 是一个基于 Python 的 ETL 框架，支持流数据处理、实时分析、机器学习管道（LLM）和检索增强生成（RAG），底层采用高性能 Rust 引擎，可处理批处理与流式数据。  

**使用方法**：通过 `pip install pathway` 安装，使用 Python API 编写处理逻辑（如实时计算正值总和），通过 `pw.run()` 启动计算，支持本地运行、Docker 部署及 Kubernetes 云扩展。  

**主要特性**：  
1. **多场景支持**：兼容批处理与流式数据，提供丰富的连接器（如数据库、消息队列）。  
2. **高效引擎**：基于 Rust 实现，支持多线程、分布式计算，性能优于 Flink、Spark 等工具。  
3. **持久化与一致性**：支持结果持久化存储，确保数据处理可靠性。  
4. **LLM 集成**：提供与 LangChain、LlamaIndex 等框架的协作能力，简化 AI 应用开发。  
5. **部署灵活**：支持本地、Docker、Kubernetes 部署，企业版支持云原生扩展。  

**许可证**：采用 BSL 1.1 许可，允许非商业免费使用，部分代码库开源（MIT/Apache 2.0）。