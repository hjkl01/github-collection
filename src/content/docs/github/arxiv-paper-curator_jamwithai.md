
---
title: arxiv-paper-curator
---

### [jamwithai arxiv-paper-curator](https://github.com/jamwithai/arxiv-paper-curator)  ![GitHub Repo stars](https://img.shields.io/github/stars/jamwithai/arxiv-paper-curator?style=social)

这是一个构建生产级 RAG（检索增强生成）系统的项目，名为"arXiv 论文策展人”。核心功能包括：

1. **自动化数据管道**：自动从 arXiv 获取学术论文元数据及 PDF 内容，并进行解析存储。
2. **混合检索系统**：基于 OpenSearch 实现 BM25 关键词搜索与向量语义搜索相结合的混合检索能力。
3. **本地 RAG 应用**：集成 Ollama 本地大模型，提供流式响应和 Gradio 交互界面，用于回答研究问题。
4. **生产级优化**：包含 Langfuse 全链路追踪、Redis 高性能缓存及监控功能。
5. **智能体增强**：引入 LangGraph 构建 Agent 工作流（支持查询改写、文档评级），并集成 Telegram 机器人实现移动端交互。

项目通过 7 个阶段的教学，指导用户使用 FastAPI、Docker、PostgreSQL 等工具从零搭建完整的 AI 工程系统。