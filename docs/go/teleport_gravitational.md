### [gravitational teleport](https://github.com/gravitational/teleport)  ![GitHub Repo stars](https://img.shields.io/github/stars/gravitational/teleport?style=social)

Teleport 是一个提供基础设施连接、认证、访问控制和审计的统一平台。主要功能包括：

1.  **统一身份与单点登录 (SSO)**：为云和本地基础设施提供统一的身份层，支持人类用户和工作负载的 SSO。
2.  **无密钥安全访问**：使用短效证书替代长期密钥或密码，保护服务器、Kubernetes、数据库、Windows 桌面、Web 应用及云 API 的访问，无需 VPN 或堡垒机即可建立安全隧道。
3.  **权限与审计**：实施统一的基于角色（RBAC）和属性（ABAC）的访问控制，支持最小特权和即时访问（JIT），并记录审计 SSH、Kubernetes、数据库、RDP 和 Web 会话活动。
4.  **广泛资源支持**：兼容 SSH、Kubernetes、多种数据库、RDP、内部 Web 服务、云控制台及 Model Context Protocol (MCP) 服务器。
5.  **灵活部署**：以单一 Go 二进制文件形式，支持部署为 Linux 守护进程或 Kubernetes 应用。