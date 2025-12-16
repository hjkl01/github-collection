
---
title: deepagents
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/langchain-ai/deepagents?style=social) ](https://github.com/langchain-ai/deepagents)
### [langchain-ai deepagents](https://github.com/langchain-ai/deepagents)

**项目核心内容总结：**

**功能**  
`deepagents` 是一个开源智能代理框架，支持长周期任务处理，集成任务规划、文件系统操作、子代理委托等能力，适用于复杂工作流自动化。提供与外部工具（如网络搜索、代码执行）的扩展接口，并支持人类干预（HITL）、长期记忆存储等特性。

**使用方法**  
1. 安装依赖：`pip install deepagents` 及所需工具（如 `tavily-python`）。  
2. 配置 API 密钥（如网络搜索工具）。  
3. 通过 `create_deep_agent` 创建代理，可自定义模型、系统提示、工具、中间件等。  
4. 调用代理执行任务，支持流式输出、子任务委托、文件操作等。  

**主要特性**  
- **内置工具**：任务管理（`write_todos`）、文件操作（`ls`/`read_file`）、代码执行（`execute`）、子代理委托（`task`）。  
- **扩展性**：支持自定义工具、中间件（如 HITL 人类审批）、后端存储（如持久化文件）。  
- **长期记忆**：通过 `CompositeBackend` 实现跨会话数据持久化。  
- **中间件机制**：自动注入工具使用规则、任务规划指引、上下文摘要等。  
- **CLI 支持**：提供交互式命令行界面，集成技能、记忆与 HITL 流程。  

**适用场景**  
复杂研究任务、代码开发、跨工具协作、需人工审核的敏感操作等。