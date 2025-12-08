
---
title: trpc-agent-go
---

### [trpc-group trpc-agent-go](https://github.com/trpc-group/trpc-agent-go)

**项目核心内容总结：**  

tRPC-Agent-Go 是一个基于 Go 语言构建的智能应用开发框架，支持集成多种大语言模型（如 OpenAI、DeepSeek）和工具（如函数、MCP、DuckDuckGo 等），提供记忆管理（支持内存和 Redis）、知识检索（RAG）、执行流程管理（Runner、Agent、Planner）及多代理协作（ChainAgent、ParallelAgent、CycleAgent）等功能。  

**主要功能与特性：**  
1. **多模型与工具支持**：兼容多种 LLM 模型，集成搜索、文件操作、代码执行等工具。  
2. **记忆与知识管理**：支持长期记忆存储及 RAG 知识检索，增强交互上下文理解。  
3. **灵活的代理协作**：通过 ChainAgent、ParallelAgent 等实现线性、并行或循环任务流程。  
4. **执行与监控**：提供 Runner 管理执行流程，集成 OpenTelemetry 实现遥测跟踪。  
5. **MCP 协议支持**：兼容 Model Context Protocol，支持结构化提示与动态工具调用。  
6. **调试与扩展**：包含调试服务器示例，支持自定义指令、会话管理和代码扩展。  

**使用方法：**  
- 运行示例代码（如 LLM 代理、多代理协作、图形工作流）。  
- 配置内存服务、知识库及遥测导出。  
- 通过 Runner 执行代理任务，支持实时调试与监控。