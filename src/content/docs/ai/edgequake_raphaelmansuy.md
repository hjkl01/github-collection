
---
title: edgequake
---

### [raphaelmansuy edgequake](https://github.com/raphaelmansuy/edgequake)  ![GitHub Repo stars](https://img.shields.io/github/stars/raphaelmansuy/edgequake?style=social)

EdgeQuake 是一个基于 Rust 的高性能 Graph-RAG 框架，它将文档转化为知识图谱，以实现更优的检索和生成。其核心功能包括：

1. **知识图谱构建**：通过 LLM 实现实体提取和关系映射，构建结构化的文档知识图谱。
2. **6 种查询模式**：从简单的向量相似性搜索到结合图遍历的混合查询，满足不同类型的查询需求。
3. **高性能架构**：基于 Rust 的异步 Tokio 架构，支持高并发请求，内存效率高。
4. **PDF 处理**：支持 PDF 文档的文本和视觉模式提取，包括扫描文档和复杂布局的处理。
5. **生产就绪**：提供 OpenAPI 3.0 REST API、SSE 流式传输、健康检查等功能。
6. **现代前端**：React 19 构建的交互式前端，支持图可视化和文档上传。
7. **多语言 SDK**：提供 Python、TypeScript、Rust 等多种语言的 SDK，方便集成。
8. **支持多种 LLM 提供商**：包括 OpenAI、Ollama、LM Studio 等，并支持自动检测。
9. **社区发现与图优化**：通过 Louvain 算法优化，支持主题查询和全局语义搜索。
10. **嵌入式存储**：使用 PostgreSQL AGE 和 pgvector 实现图数据和向量嵌入的高效存储。

EdgeQuake 在实体提取、查询延迟、文档处理速度和内存使用等方面均优于传统 RAG 系统，适用于需要多跳推理、主题分析和关系查询的复杂场景。