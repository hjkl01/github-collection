
---
title: archgw
---

### [katanemo archgw](https://github.com/katanemo/archgw)  ![GitHub Repo stars](https://img.shields.io/github/stars/katanemo/archgw?style=social)

Plano 是一个面向智能体应用的 AI 原生代理服务器和数据平面。它通过将路由编排、模型管理、安全护栏及可观测性等核心交付工作解耦至统一的进程外数据平面，解决智能体应用生产部署难的问题。

核心功能包括：
- **智能编排**：实现智能体间低延迟路由，通过 YAML 配置即可新增智能体，无需修改应用代码。
- **模型敏捷性**：支持按名称、别名或偏好自动路由不同大语言模型（LLM）。
- **零代码可观测**：自动捕获智能体信号及 OpenTelemetry 追踪指标，无需手动插桩。
- **安全护栏**：提供防越狱、内容审核及记忆钩子的过滤链机制。

基于 Envoy 构建，兼容任意编程语言和 AI 框架，降低开发复杂度，提升应用的安全性、可维护性与交付速度。