
---
title: teleport
---

### [gravitational teleport](https://github.com/gravitational/teleport)  ![GitHub Repo stars](https://img.shields.io/github/stars/gravitational/teleport?style=social)

Teleport 是一个用于基础设施的统一身份识别、访问控制和审计平台。

- **安全访问**：为 SSH、Kubernetes、数据库、Web 应用、云 API 及 MCP 服务器提供单点登录 (SSO)，采用基于证书的短寿命认证，无需长期密钥或密码，支持多因素认证 (MFA)。
- **网络连通**：建立无需 VPN 或堡垒机的安全通道，可穿透 NAT 和防火墙访问资源。
- **权限控制**：实施基于角色 (RBAC) 和属性 (ABAC) 的策略，支持最小权限和即时访问 (JIT)。
- **审计监控**：记录并审计所有会话活动（SSH、容器、数据库、RDP、Web 等）。
- **身份统一**：统一人类用户与工作负载的身份层，支持 Linux 守护进程或 Kubernetes 组件部署。