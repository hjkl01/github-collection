### [infiniflow ragflow](https://github.com/infiniflow/ragflow)  ![GitHub Repo stars](https://img.shields.io/github/stars/infiniflow/ragflow?style=social)

RAGFlow 是一款开源检索增强生成（RAG）引擎，融合 Agent 能力，旨在为企业构建适配大语言模型（LLM）的上下文层。核心功能包括：

1. **深度文档理解**：支持复杂格式非结构化数据（Word、PDF、图像、扫描件等）的知识提取与长文本检索。
2. **智能切片与引用**：提供模板化、可解释的文本切片方案，支持可视化干预及可追溯引用，减少生成幻觉。
3. **多源数据兼容**：兼容多种文档格式，支持 Confluence、S3、Notion 等数据源同步，集成 MinerU 与 Docling 解析。
4. **自动化工作流**：支持流式 RAG 编排，可配置 LLM 及嵌入模型，具备多重召回与重排序能力，提供直观 API。
5. **智能体能力**：支持 AI 智能体记忆、工作流编排、代码执行器及多模态图像内容理解。
6. **灵活部署**：支持 Docker 快速部署（默认 Elasticsearch，可选 Infinity 引擎）及源码开发模式。