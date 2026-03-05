
---
title: parlant
---

### [emcie-co parlant](https://github.com/emcie-co/parlant)  ![GitHub Repo stars](https://img.shields.io/github/stars/emcie-co/parlant?style=social)

Parlant 是一个面向客户 AI 代理的对话控制层，专为构建需要一致性、合规性和品牌一致性的企业级 B2C 及敏感 B2B 交互代理而设计。

其核心通过“上下文工程”技术，动态筛选并注入对话中当前最相关的规则、知识和工具，而非依赖庞大的系统提示词，从而解决提示词过载和路由图脆弱的问题。代理行为通过代码定义，而非提示词。

主要功能包括：
*   **指南（Guidelines）**：条件 - 动作对的行为规则，引擎仅匹配当前相关规则。
*   **关系（Relationships）**：处理规则间的依赖与排除，保持上下文聚焦。
*   **旅程（Journeys）**：适应客户交互状态的多步标准操作程序（SOP）。
*   **预置回复（Canned Responses）**：关键时刻使用预批准模板，消除幻觉。
*   **工具（Tools）**：仅在观测条件匹配时触发外部 API，避免误调用。
*   **术语表（Glossary）**：映射特定领域词汇，理解客户语言。
*   **可解释性（Explainability）**：全链路 OpenTelemetry 追踪记录决策。

项目提供 Python SDK，行为配置与 LLM 提供商无关，并可作为控制层与 LangGraph 等现有框架集成使用。