
---
title: kagent
---

### [kagent-dev kagent](https://github.com/kagent-dev/kagent)  ![GitHub Repo stars](https://img.shields.io/github/stars/kagent-dev/kagent?style=social)

kagent 是一个 Kubernetes 原生的 AI 代理构建框架，旨在简化 AI 代理在 Kubernetes 中的构建、部署和管理流程。

主要功能：
- **声明式管理**：通过 Kubernetes 自定义资源（Agent、ModelConfig、ToolServers）定义代理、模型配置及工具。
- **多模型支持**：兼容 OpenAI、Azure、Anthropic、Google Vertex AI、Ollama 等多种大语言模型提供商。
- **工具集成**：支持 MCP 协议，提供 Kubernetes、Istio、Helm、Prometheus 等运维工具。
- **核心架构**：包含控制平面（Controller）、Web 管理界面（UI）、基于 Google ADK 的运行引擎（Engine）及命令行工具（CLI）。
- **可观测性**：支持 OpenTelemetry 追踪，便于监控代理与工具的运行状态。

项目遵循云原生、可扩展、灵活及可测试的设计原则。