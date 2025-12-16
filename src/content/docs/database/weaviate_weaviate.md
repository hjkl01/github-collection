
---
title: weaviate
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/weaviate/weaviate?style=social) ](https://github.com/weaviate/weaviate)
### [weaviate weaviate](https://github.com/weaviate/weaviate)

**项目核心内容总结：**

**1. 项目功能**  
Weaviate 是一个开源的云原生向量数据库，支持对象和向量存储，提供语义搜索、关键词过滤、检索增强生成（RAG）及重排序功能，适用于构建推荐系统、语义搜索、多模态应用等场景。

**2. 使用方法**  
- **部署方式**：支持 Docker、Kubernetes、云平台（如 AWS、Google）及 Weaviate Cloud 部署。  
- **开发集成**：提供 Python、TypeScript 等语言的客户端库，通过 API 实现数据存储与查询。  
- **示例流程**：使用 Docker Compose 部署，通过 Python 代码创建数据集合、插入数据并执行语义搜索（示例代码已提供）。

**3. 主要特性**  
- **高效搜索**：结合向量相似度（如余弦相似度）与关键词（BM25）的混合搜索，支持多模态数据。  
- **扩展性**：支持大规模数据存储与高并发查询，适配企业级应用。  
- **AI 集成**：内置 RAG 框架，支持与 LLM（如 LangChain、LlamaIndex）及 Agent 工具（如 CrewAI、Dynamiq）集成。  
- **成本优化**：通过向量化压缩技术降低存储与计算资源消耗。  
- **生态支持**：兼容 Airbyte、Databricks 等数据平台，及 Comet、LangWatch 等 AI 监控工具。