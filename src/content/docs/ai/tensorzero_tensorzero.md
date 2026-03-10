
---
title: tensorzero
---

### [tensorzero tensorzero](https://github.com/tensorzero/tensorzero)  ![GitHub Repo stars](https://img.shields.io/github/stars/tensorzero/tensorzero?style=social)

TensorZero 是一个开源的工业级大语言模型（LLM）应用平台，提供统一的 API 网关、可观测性、优化、评估和实验等功能。其核心功能包括：

1. **LLM 网关**：通过统一的 API 访问所有主流 LLM 提供商，支持多种推理方式（如流式、工具调用、结构化输出、批量处理等），并提供高吞吐量和低延迟（<1ms p99）。

2. **LLM 可观测性**：记录推理过程和反馈数据，支持通过 UI 或程序访问，便于调试和监控，同时支持导出 OpenTelemetry 和 Prometheus 数据。

3. **LLM 优化**：利用生产数据和用户反馈优化提示词、模型和推理策略，支持监督微调、动态上下文学习等技术。

4. **LLM 评估**：通过启发式规则和 LLM 判断进行推理和端到端工作流的评估，支持 A/B 测试和评估指标分析。

5. **LLM 实验**：内置 A/B 测试、路由、回退等功能，支持多轮交互系统和顺序测试，提升部署信心。

6. **扩展性与集成**：支持多种编程语言，提供 GitOps 友好部署、第三方工具集成、自定义扩展能力，并提供交互式提示测试界面。

TensorZero 是一个全面的 LLMOps 平台，适用于从原型开发到复杂部署的各类大语言模型应用。