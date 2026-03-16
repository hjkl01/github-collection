### [HKUDS LightRAG](https://github.com/HKUDS/LightRAG)  ![GitHub Repo stars](https://img.shields.io/github/stars/HKUDS/LightRAG?style=social)

LightRAG 是一款简单且高效的检索增强生成（RAG）系统，通过整合知识图谱技术提升信息检索与生成的质量。其主要功能包括：

1. **知识图谱检索**：结合局部与全局检索模式，利用知识图谱增强上下文理解，支持混合查询以提升回答准确性。
2. **多模态支持**：集成 RAG-Anything，支持文本、图像、表格、公式及多种文档格式（PDF、Office 等）的解析与处理。
3. **灵活存储与部署**：支持多种存储后端（JSON、PostgreSQL、Redis、MongoDB、Neo4j 等），提供 Web UI、REST API 及 Docker 部署方案。
4. **模型兼容**：兼容各类 LLM 和嵌入模型（如 OpenAI、Ollama、Hugging Face、Azure 等），支持自定义注入。
5. **图谱管理**：支持实体的增删改查、合并操作，以及关系的管理，具备引用溯源和 Citation 功能。
6. **评估与追踪**：集成 RAGAS 评估框架和 Langfuse 可观测性工具，支持 Token 消耗追踪。
7. **数据隔离**：通过工作空间（Workspace）实现多实例间的数据隔离与安全管理。