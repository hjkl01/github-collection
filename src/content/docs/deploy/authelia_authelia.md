
---
title: authelia
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/authelia/authelia?style=social) ](https://github.com/authelia/authelia)
### [authelia authelia](https://github.com/authelia/authelia)

**核心内容总结：**  
Authelia 是一个基于 Go 的开源多因素认证（MFA）解决方案，用于保护 Web 应用和 API 的用户身份验证。其主要功能包括支持 TOTP、FIDO2、WebAuthn 等认证方式，提供基于角色的访问控制（RBAC）、会话管理、审计日志和与 OAuth2/OpenID Connect 协议的集成。  

**使用方法：**  
- 通过 YAML 配置文件定义认证策略和用户权限；  
- 与代理服务器（如 Nginx、Traefik、Caddy 等）集成，实现反向代理认证；  
- 支持 Docker 和 Kubernetes 部署，便于容器化环境使用。  

**主要特性：**  
1. 多种认证方式：TOTP、FIDO2、WebAuthn、YubiKey 等；  
2. 与常见代理服务器兼容，支持灵活的网络架构；  
3. 提供细粒度的访问控制和用户会话管理；  
4. 开源且遵循 Apache 2.0 协议，社区活跃。