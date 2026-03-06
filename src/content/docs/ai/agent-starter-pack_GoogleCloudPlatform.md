
---
title: agent-starter-pack
---

### [GoogleCloudPlatform agent-starter-pack](https://github.com/GoogleCloudPlatform/agent-starter-pack)  ![GitHub Repo stars](https://img.shields.io/github/stars/GoogleCloudPlatform/agent-starter-pack?style=social)

Agent Starter Pack 是一个为 Google Cloud 生成式 AI 代理提供生产就绪模板的 Python 包，旨在让开发者专注于代理逻辑，而由工具包提供基础设施、CI/CD、可观测性和安全配置。

核心功能：
1. 预置模板：支持 ReAct、RAG、多代理及实时对话等多种架构，兼容 ADK 和 LangGraph。
2. 快速部署：通过命令一键创建或增强项目，自动生成后端、前端及部署基础设施，支持 Cloud Run 和 Agent Engine。
3. 自动化运维：集成 CI/CD 流水线、监控、可观测性及 RAG 数据管道，支持 Vertex AI 评估。
4. 开发辅助：集成 Gemini CLI，支持远程模板共享及自定义扩展。

环境要求：Python 3.10+、Google Cloud SDK、Terraform 和 Make。