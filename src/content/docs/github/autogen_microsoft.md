
---
title: autogen
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/autogen?style=social) ](https://github.com/microsoft/autogen)
### [microsoft autogen](https://github.com/microsoft/autogen)

**AutoGen 核心内容总结**  

**项目功能**  
AutoGen 是一个用于构建多智能体 AI 应用的框架，支持智能体自主运行或与人类协作，适用于复杂任务的自动化处理。  

**使用方法**  
1. **安装**：需 Python 3.10 及以上版本，通过 pip 安装核心包及扩展（如 OpenAI 客户端）。  
2. **快速入门**：  
   - **基础示例**：使用 OpenAI 模型创建助理智能体（如“Hello World”）。  
   - **MCP 服务器**：集成 Playwright 实现网页浏览功能。  
   - **多智能体协作**：通过 `AgentTool` 调用不同领域的专家智能体（如数学、化学）。  
   - **无代码工具**：AutoGen Studio 提供图形化界面简化开发流程。  

**主要特性**  
- **分层架构**：包含核心 API（跨语言支持）、AgentChat API（Python 专用）和 Extensions API（功能扩展）。  
- **多语言支持**：提供 Python 和 .NET（C#）版本的库和文档。  
- **开发工具**：集成 AutoGen Studio（无代码开发）、AutoGen Bench（性能测试）等。  
- **可扩展性**：支持自定义智能体、插件及与其他系统的集成（如 Grpc 通信）。  

**适用场景**  
适用于需要多智能体协作的复杂任务，如自动化客服、数据分析、科研模拟等。