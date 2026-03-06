
---
title: warpgate
---

### [warp-tech warpgate](https://github.com/warp-tech/warpgate)  ![GitHub Repo stars](https://img.shields.io/github/stars/warp-tech/warpgate?style=social)

Warpgate 是一款智能且完全透明的 SSH、HTTPS、MySQL 和 PostgreSQL 堡垒机，部署于 DMZ 区域。它无需客户端或 SSH 包装器，直接代理连接至目标服务。

核心特性：
1. **透明连接**：非跳板机模式，客户端无感知，支持标准协议及非交互式连接。
2. **会话审计**：内置 Web 管理界面，支持会话实时查看、回放及日志存储（SQLite）。
3. **权限管理**：支持将用户精确分配给特定主机或 URL。
4. **安全认证**：原生支持 2FA 和 SSO（TOTP & OpenID Connect）。
5. **技术架构**：100% 安全的 Rust 编写，单二进制文件无依赖，生产就绪。