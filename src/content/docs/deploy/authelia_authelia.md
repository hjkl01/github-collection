
---
title: authelia
---

### [authelia authelia](https://github.com/authelia/authelia)  ![GitHub Repo stars](https://img.shields.io/github/stars/authelia/authelia?style=social)

Authelia 是一款开源的身份认证和授权服务器，通过 Web 门户为应用程序提供双因素认证 (2FA) 和单点登录 (SSO) 服务。它作为反向代理的辅助组件，用于控制请求的允许、拒绝或重定向。

核心功能：
1. 支持 OpenID Connect 1.0 和 OAuth 2.0 协议。
2. 提供多种认证方式：FIDO2/WebAuthn 安全密钥、TOTP、移动推送通知及无密码认证。
3. 基于子域名、用户、组、URI 等条件的细粒度访问控制。
4. 支持密码重置、登录失败锁定及高可用部署。
5. 兼容 Nginx、Traefik、Caddy 等多种反向代理及 Kubernetes 环境。