
---
title: arxiv-paper-curator
---

### [jamwithai arxiv-paper-curator](https://github.com/jamwithai/arxiv-paper-curator)  ![GitHub Repo stars](https://img.shields.io/github/stars/jamwithai/arxiv-paper-curator?style=social)

本项目是"The Mother of AI Project"的第一阶段，名为"arXiv Paper Curator"，旨在通过实战帮助用户从零构建生产级 RAG（检索增强生成）系统。

核心功能如下：
1. **自动化数据管道**：自动从 arXiv 获取、解析学术论文元数据及 PDF 内容并存入数据库。
2. **混合检索引擎**：首先实现基于 BM25 的关键词搜索，随后结合向量嵌入实现混合检索。
3. **智能问答系统**：集成本地 LLM（Ollama），支持流式响应、语义理解及 Gradio 交互界面。
4. **生产级运维**：包含服务编排（Docker/Airflow）、全链路监控（Langfuse）、性能缓存（Redis）及健康检查。
5. **智能体增强**：基于 LangGraph 实现自适应检索策略、文档评估、查询重写，并提供 Telegram 机器人支持移动端访问。

项目遵循“先搜索基础后 AI 增强”的工业级开发路径，提供从基础设施到高级智能体的分周代码与教学指南。