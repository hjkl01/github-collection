
---
title: convoy
---

### [frain-dev convoy](https://github.com/frain-dev/convoy)  ![GitHub Repo stars](https://img.shields.io/github/stars/frain-dev/convoy?style=social)

Convoy 是一个开源的高性能 Webhooks 网关，用于安全地摄取、持久化、调试、投递和管理海量事件。

核心功能：
- **Webhooks 网关**：位于网络边缘，流式传输及路由 Webhooks，保护内部系统不暴露于公网。
- **可扩展性**：支持水平扩展，API 服务器、工作器等组件可独立伸缩。
- **安全性**：支持载荷签名、Bearer 令牌认证及静态 IP 设置。
- **投递控制**：支持基于事件类型的扇出、端点级速率限制。
- **重试机制**：支持恒定时长与指数退避重试算法，以及批量重试。
- **客户仪表板**：提供可嵌入的客户侧仪表板，支持调试、重试及端点配置。
- **失败通知**：端点连续失败时自动禁用并发送 Email 或 Slack 通知。

支持通过 Docker 和 Kubernetes (Helm) 进行部署。