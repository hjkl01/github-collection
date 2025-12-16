
---
title: agno
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/agno-agi/agno?style=social) ](https://github.com/agno-agi/agno)
### [agno-agi agno](https://github.com/agno-agi/agno)

**项目核心内容总结：**

**项目功能**  
Agno 是一个高性能的多智能体系统框架，提供从开发、运行到管理的完整解决方案。包含三大核心模块：  
1. **框架**：支持构建智能体、团队和工作流，集成记忆、知识、状态管理、人机协作（HITL）、上下文压缩、模型上下文协议（MCP）、智能体间通信（A2A）等功能。  
2. **AgentOS 运行时**：提供安全、无状态的生产级运行环境，内置 FastAPI 应用，可直接部署。  
3. **AgentOS 控制平面**：通过可视化界面实时测试、监控和管理多智能体系统。  

**使用方法**  
- 新手可通过官方文档的[快速入门指南](https://docs.agno.com/get-started/quickstart)创建首个智能体，并通过 AgentOS UI 进行交互。  
- 示例代码提供 Python 脚本模板，集成数据库、MCP 服务器和 FastAPI 应用。  
- 提供[示例库](https://docs.agno.com/examples/use-cases/agents/overview)辅助开发实际应用。  

**主要特性**  
- **开发友好**：支持 100+ 模型，类型安全，动态上下文管理，集成 RAG（检索增强生成）技术。  
- **性能优化**：智能体实例化时间低至 3 微秒，内存占用仅为 6.6KiB，远超 LangGraph、CrewAI 等框架。  
- **安全隐私**：无状态设计，支持通过环境变量关闭 telemetry 日志。  
- **扩展性强**：支持 IDE 集成（如 Cursor），通过 `llms.txt` 文件提升 AI 对文档的理解效率。