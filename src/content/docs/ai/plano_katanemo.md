
---
title: plano
---

### [katanemo plano](https://github.com/katanemo/plano)  ![GitHub Repo stars](https://img.shields.io/github/stars/katanemo/plano?style=social)

Plano 是一个面向智能体（Agentic）应用的 AI 原生代理服务器和数据平面，旨在解决将智能体应用安全、可靠地部署到生产环境的难题。它将路由编排、安全过滤、观测性等核心逻辑集中到一个无进程的数据平面中，实现与框架无关的解耦。

核心功能：
1. **智能体编排**：通过 YAML 声明式配置代理描述，实现低延迟的代理间路由，添加新代理无需修改应用代码。
2. **模型敏捷路由**：支持按模型名称、别名或智能偏好自动路由，统一不同模型供应商的 API 接口。
3. **零代码观测**：自动捕获全链路 OpenTelemetry 跟踪、指标及智能体信号，支持持续评估与改进。
4. **安全与记忆钩子**：通过过滤器链（Filter Chains）构建防越狱、内容审核和记忆管理功能。
5. **灵活集成**：支持任何语言或框架，代理只需是兼容 OpenAI 标准的 HTTP 服务器。

该项目基于 Envoy 构建，利用轻量级 LLM 进行路由决策，旨在帮助开发者以更低成本、更低延迟快速交付生产级智能体应用。