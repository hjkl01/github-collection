
---
title: pydantic-ai
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/pydantic/pydantic-ai?style=social) ](https://github.com/pydantic/pydantic-ai)
### [pydantic pydantic-ai](https://github.com/pydantic/pydantic-ai)

**项目核心内容总结：**  
Pydantic AI 是一个基于 Python 的生成式 AI 代理框架，旨在帮助开发者高效构建生产级应用和工作流程。其核心功能包括：  
1. **模型无关性**：支持主流模型（如 OpenAI、Anthropic、Gemini 等）及云服务（Azure、AWS 等），可自定义模型。  
2. **类型安全**：通过 Pydantic 验证实现编译时类型检查，减少运行时错误。  
3. **可观测性集成**：与 Pydantic Logfire 深度整合，支持实时调试、性能监控和成本追踪。  
4. **工具与依赖注入**：通过装饰器注册工具函数，结合依赖注入实现动态指令和复杂业务逻辑（如银行客服场景示例）。  
5. **持久化执行与流式输出**：支持断点续传、异步流程，以及结构化数据的实时流式输出。  
6. **评估与图支持**：提供系统化评估工具，支持通过类型提示定义复杂应用的图结构。  

**使用方法**：  
- 安装包后，通过 `Agent` 类定义代理，设置模型、指令、输出类型等参数。  
- 使用装饰器（如 `@tool`、`@instructions`）扩展功能，结合依赖注入实现动态逻辑。  
- 参考文档中的示例（如银行客服场景）快速上手。  

**主要特性**：  
- 由 Pydantic 团队开发，兼容主流 AI 生态。  
- 支持工具审批、人机协作流程、多模型提供商。  
- 提供静态类型检查、评估框架、持久化执行等生产级特性。