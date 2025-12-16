
---
title: warpgate
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/warp-tech/warpgate?style=social) ](https://github.com/warp-tech/warpgate)
### [warp-tech warpgate](https://github.com/warp-tech/warpgate)

**项目核心内容总结：**  
Warpgate 是一个基于 Rust 的智能堡垒主机，支持 SSH、HTTPS、MySQL 和 PostgreSQL 协议，无需客户端或 SSH 包装器即可实现安全访问控制。  

**主要功能：**  
- 部署于 DMZ 环境，通过用户账户分配实现对内网主机/URL 的精准访问控制。  
- 全透明连接：直接转发用户流量至目标主机，客户端无需额外配置。  
- 内置 Web 管理界面，支持实时会话监控、历史回放及日志审计。  
- 原生支持 2FA（TOTP）和 SSO（OpenID Connect）。  
- 单文件部署，无依赖项，兼容 Docker。  

**使用方法：**  
1. 通过 [官方文档](https://warpgate.null.page/getting-started/) 或 Docker 部署。  
2. 下载发布版（[Release](https://github.com/warp-tech/warpgate/releases)）或夜间构建版本（[Nightly](https://nightly.link/warp-tech/warpgate/workflows/build/main)）。  
3. 使用 `warpgate setup` 命令生成配置文件，设置端口绑定及用户/目标映射关系。  

**核心特性：**  
- **安全审计**：支持命令级审计与全会话录制（存储于 SQLite 数据库）。  
- **对比优势**：相比跳板机、VPN 和 Teleport，提供更精细的用户-服务映射、无需自定义客户端、原生 2FA/SSO 及自托管数据所有权。  
- **技术栈**：Rust（SSH、HTTP、数据库）、TypeScript（Web 界面），支持 OpenAPI 自动生成 SDK。