
---
title: gatus
---

### [TwiN gatus](https://github.com/TwiN/gatus)  ![GitHub Repo stars](https://img.shields.io/github/stars/TwiN/gatus?style=social)

Gatus 是一个面向开发者的健康监控仪表盘，用于主动监控服务的可用性和性能。它支持通过 HTTP、ICMP、TCP、DNS、gRPC 等多种协议进行健康检查，并允许配置丰富的条件（如状态码、响应时间、证书过期时间、响应内容等）。当监控失败达到阈值时，Gatus 可通过 Slack、PagerDuty、Email、短信等数十种渠道发送警报。项目提供 Web 界面展示实时监控状态，支持 Prometheus 指标导出、状态徽章生成、维护窗口设置、安全认证（Basic Auth、OIDC）及动态配置热重载等功能。其核心理念是在客户端发现问题前主动识别服务异常，弥补传统被动监控的不足。