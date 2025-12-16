
---
title: arxiv-paper-curator
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/jamwithai/arxiv-paper-curator?style=social) ](https://github.com/jamwithai/arxiv-paper-curator)
### [jamwithai arxiv-paper-curator](https://github.com/jamwithai/arxiv-paper-curator)

**项目核心内容总结：**

本项目是一个完整的生产级RAG（检索增强生成）系统开发教程，包含7周课程，逐步构建从数据抓取、搜索、缓存到智能代理的AI应用。主要功能包括：

1. **系统架构**  
   - 基于FastAPI构建RESTful API，集成PostgreSQL存储数据，OpenSearch实现混合搜索（BM25+向量），Airflow管理任务流程。
   - Week4后使用Jina AI生成嵌入向量，Week5通过Ollama部署本地大模型，Week6引入Redis缓存和Langfuse监控，Week7集成Telegram机器人并实现LangGraph智能代理。

2. **核心功能**  
   - 支持关键词搜索（BM25）、混合搜索（BM25+向量）、缓存优化、请求追踪、智能代理（多步骤决策、文档评分、查询重写）及Telegram交互。

3. **使用方法**  
   - 克隆代码后配置.env文件，通过`docker compose up`启动服务，使用`make start`管理容器。
   - 通过API端点（如`/api/v1/hybrid-search`）调用功能，或运行Notebook逐步学习各阶段内容。

4. **主要特性**  
   - 分阶段学习：从基础环境搭建到高级智能代理，覆盖全栈开发。
   - 技术栈完整：集成主流AI工具（如LangGraph、Jina AI）和监控方案。
   - 生产级优化：包含缓存、监控、多语言支持及Telegram移动端交互。