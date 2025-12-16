
---
title: ragflow
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/infiniflow/ragflow?style=social) ](https://github.com/infiniflow/ragflow)
### [infiniflow ragflow](https://github.com/infiniflow/ragflow)

**项目核心内容总结：**

**功能**  
RAGFlow 是一个基于检索增强生成（RAG）的系统，结合深度文档处理（DeepDoc）和向量数据库，支持文档解析、向量化存储及检索，适用于知识管理、信息检索等场景。提供 Elasticsearch 和 Infinity 两种文档引擎选择，支持自定义 LLM 和嵌入模型。

**使用方法**  
1. **Docker 部署**：通过 `docker-compose.yml` 启动服务，支持 CPU/GPU 加速 DeepDoc 任务，可切换文档引擎（如 Infinity）。  
2. **源码开发**：需安装 Python 依赖、启动 MinIO/MySQL/Elasticsearch 等依赖服务，运行后端和前端（需 npm 安装并启动前端）。  

**主要特性**  
- 支持多种文档引擎（Elasticsearch/Infinity）和 LLM 厂商自定义配置。  
- 深度文档处理（OCR、格式转换、多语言支持）。  
- 向量化存储与高效检索（支持 GPU 加速）。  
- 灵活的配置选项（如 HTTP 端口、API 密钥）。  
- 提供稳定版本（如 v0.21.1）和轻量版（slim）选择。