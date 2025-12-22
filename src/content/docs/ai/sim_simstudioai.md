
---
title: sim
---

### [simstudioai sim](https://github.com/simstudioai/sim)  ![GitHub Repo stars](https://img.shields.io/github/stars/simstudioai/sim?style=social)

**项目功能：**  
Sim 是一个基于 AI 的协作平台，支持知识库、代码生成、实时协作等功能，适用于开发、学习和团队协作场景。

**使用方法：**  
- **Docker 部署：** 使用 `docker-compose` 快速部署，支持 Ollama、vLLM 等本地模型，也可连接外部 AI 服务。  
- **开发环境：** 支持 VS Code Dev Container 和 Bun 运行时，便于本地开发。  
- **手动部署：** 需要 PostgreSQL 数据库（支持 pgvector 扩展），并配置相关环境变量。

**主要特性：**  
- 支持本地 AI 模型（如 Ollama、vLLM），无需依赖外部 API。  
- 提供 Copilot 功能，需通过 sim.ai 生成 API 密钥。  
- 使用 PostgreSQL + pgvector 实现知识库和语义搜索。  
- 基于 Next.js、Bun、Drizzle ORM、Socket.io 等技术栈构建。  
- 支持多人实时协作、代码执行、流程编辑等功能。

**注意事项：**  
- 使用 Docker 时，若 Ollama 在宿主机运行，需将 `OLLAMA_URL` 设置为 `http://host.docker.internal:11434`。  
- 数据库需配置 pgvector 扩展，建议使用 Docker 部署数据库。  
- 环境变量需正确配置，包括数据库连接、认证密钥、应用地址等。