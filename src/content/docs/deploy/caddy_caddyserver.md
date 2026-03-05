
---
title: caddy
---

### [caddyserver caddy](https://github.com/caddyserver/caddy)  ![GitHub Repo stars](https://img.shields.io/github/stars/caddyserver/caddy?style=social)

Caddy 是一个基于 Go 语言的可扩展服务器平台，默认启用 TLS/HTTPS。核心功能包括：

- **自动 HTTPS**：默认自动配置和管理证书（支持 ZeroSSL、Let's Encrypt 及本地内部 CA），支持集群协调与加密客户端 Hello。
- **灵活配置**：支持 Caddyfile 简易配置、JSON 原生配置及动态 API 调整，提供适配器支持 YAML、NGINX 等多种格式。
- **高性能与扩展**：默认支持 HTTP/1.1/2/3，模块化架构无外部依赖，具备高可扩展的插件系统。
- **通用性**：不仅作为 Web 服务器，还可作为运行任何长运行 Go 程序的平台。
- **高可靠性**：生产级稳定，能抵御 TLS/OCSP 等问题导致的服务中断。