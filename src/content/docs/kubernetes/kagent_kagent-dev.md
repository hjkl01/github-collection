
---
title: kagent
---

### [kagent-dev kagent](https://github.com/kagent-dev/kagent)

**项目功能**  
kagent 是一个基于 Kubernetes 的 AI 代理框架，用于构建、部署和管理 AI 代理。支持多种大语言模型（LLM）提供商（如 OpenAI、Azure OpenAI、Anthropic 等），并提供 Kubernetes 原生工具（如 Kubernetes、Istio、Prometheus 等）的集成能力，支持可观测性（OpenTelemetry 跟踪）。

**使用方法**  
- 通过 [Quick Start](https://kagent.dev/docs/kagent/getting-started/quickstart) 快速入门  
- 参考 [安装指南](https://kagent.dev/docs/kagent/introduction/installation) 部署  

**主要特性**  
1. **Kubernetes 原生**：基于 Kubernetes 自定义资源（CRD）定义代理和工具，声明式配置。  
2. **可扩展**：支持自定义 LLM 提供商和工具，兼容多种 AI 网关。  
3. **灵活**：适配各种 AI 代理使用场景，提供丰富的工具集（如 Helm、Argo 等）。  
4. **可观测**：集成 OpenTelemetry，支持监控和调试。  
5. **组件架构**：包含控制器（Controller）、UI 界面、ADK 引擎和 CLI 工具。  

**其他**  
- 开源协议：Apache 2.0  
- 社区资源：提供 Discord 论坛、贡献指南和 Roadmap。