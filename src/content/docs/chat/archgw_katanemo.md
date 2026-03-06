
---
title: archgw
---

### [katanemo archgw](https://github.com/katanemo/archgw)  ![GitHub Repo stars](https://img.shields.io/github/stars/katanemo/archgw?style=social)

Plano 是一个面向智能体应用的 AI 原生代理服务器和数据平面，旨在解决智能体应用从原型到生产环境部署的复杂性问题。它通过将核心交付关注点（编排、模型管理、可观测性）移入统一的进程外数据平面，使开发者能专注于核心业务逻辑。其核心功能包括：

1. **智能体编排**：支持低延迟智能体间路由，新增智能体无需修改应用代码。
2. **模型敏捷性**：提供统一 LLM 路由 API，支持按模型名、别名或偏好自动路由。
3. **可观测性**：零代码捕获 OpenTelemetry 追踪、指标及智能体信号。
4. **安全护栏**：内置内容审核、防越狱保护及记忆钩子过滤器。

Plano 基于 Envoy 构建，支持任意编程语言或 AI 框架，通过 YAML 配置即可实现意图分类、路由逻辑和追踪，加速智能体应用的高效上线。