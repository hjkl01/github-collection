
---
title: agent-starter-pack
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/GoogleCloudPlatform/agent-starter-pack?style=social) ](https://github.com/GoogleCloudPlatform/agent-starter-pack)
### [GoogleCloudPlatform agent-starter-pack](https://github.com/GoogleCloudPlatform/agent-starter-pack)

**核心内容总结：**  
Agent Starter Pack 是一个 Python 工具包，提供在 Google Cloud 上构建生成式 AI 代理的生产级模板，包含基础设施、CI/CD、可观测性和安全功能，用户仅需专注代理逻辑。  

**功能与特性：**  
- **代理模板**：支持 ReAct、RAG（文档检索问答）、多代理、实时多模态交互等模式，适配 Vertex AI Search/Vector Search 等服务。  
- **部署与运维**：通过 Cloud Run 或 Agent Engine 部署，集成监控、日志和 CI/CD 流水线（支持 Cloud Build 和 GitHub Actions）。  
- **开发工具**：集成 Gemini CLI，提供代码建议；支持 Terraform 自动化数据管道（如 RAG 嵌入处理）。  
- **扩展性**：支持自定义模板，可结合 ADK（Agent Development Kit）或 LangGraph 框架。  

**使用方法：**  
1. 安装：通过 `uvx agent-starter-pack create 项目名` 或 pip 安装后使用命令创建项目。  
2. 增强现有项目：在项目根目录运行 `uvx agent-starter-pack enhance` 添加生产级基础设施。  
3. 文档与示例：提供详细部署指南、社区案例及视频教程，支持 Firebase Studio 和 Cloud Shell 快速启动。  

**要求：** 需 Python 3.10+、Google Cloud SDK、Terraform 和 Make 工具。