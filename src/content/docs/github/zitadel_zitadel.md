
---
title: zitadel
---

### [zitadel zitadel](https://github.com/zitadel/zitadel)

**核心内容总结：**  
ZITADEL 是一个开源的身份管理平台，提供多租户用户管理、自服务功能及多种认证协议支持（如 OpenID Connect、OAuth2、SAML、LDAP 等），适用于企业级应用。  

**主要功能：**  
- **身份验证**：支持密码、Passkeys（FIDO 2/WebAuthN）、第三方登录及令牌交换。  
- **多租户管理**：支持身份代理、自定义企业入驻流程、角色权限委托及域名自动发现。  
- **集成能力**：提供 GRPC/REST API、SCIM 2.0 服务器、RBAC 权限控制及与外部审计系统对接。  
- **自助服务**：用户可自行注册、管理账户，管理员可通过控制台（Console）管理组织、项目和应用。  
- **部署方式**：支持自托管（PostgreSQL 数据库、零停机更新、高可用架构）及云服务（ZITADEL Cloud，含免费层级和按需付费）。  

**使用方法：**  
1. **自托管**：通过 Docker、Kubernetes 或直接部署在 Linux/MacOS 系统，配置 PostgreSQL 数据库。  
2. **云服务**：注册 ZITADEL Cloud，使用 SaaS 模式快速部署，按需扩展功能。  

**核心特性：**  
- API 优先设计，支持全功能接口调用。  
- 事件溯源（Event Sourcing）存储架构，保障数据可靠性。  
- 提供 SDK 示例和开发者文档，便于集成。  
- 支持高安全性设计（如零停机更新、审计日志）。