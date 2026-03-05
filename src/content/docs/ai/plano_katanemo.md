
---
title: plano
---

### [katanemo plano](https://github.com/katanemo/plano)  ![GitHub Repo stars](https://img.shields.io/github/stars/katanemo/plano?style=social)

Plano 是面向智能体应用的 AI 原生代理服务器和数据平面，旨在简化智能体应用的安全、可靠生产部署。它基于 Envoy 构建，将路由编排、模型管理、安全护栏及可观测性从应用代码中解耦，迁移至统一的外部数据平面。

核心功能：
- **智能体编排**：支持低延迟的多智能体协调，通过 YAML 声明式配置即可添加智能体，无需修改应用代码。
- **模型路由**：灵活支持按模型名称、别名或偏好自动进行 LLM 路由。
- **自动可观测**：零代码捕获智能体信号及 OpenTelemetry 追踪与指标。
- **安全与护栏**：通过过滤器链提供防越狱、内容审核及内存管理策略。
- **框架无关**：兼容任意编程语言及 AI 框架，智能体仅需实现标准 HTTP 接口。

该工具帮助开发者消除繁琐的中间件工作，利用轻量级 LLM 实现高效路由，加速智能体应用落地生产。