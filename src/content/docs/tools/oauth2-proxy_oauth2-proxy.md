
---
title: oauth2-proxy
---

### [oauth2-proxy oauth2-proxy](https://github.com/oauth2-proxy/oauth2-proxy)

OAuth2-Proxy 是一个灵活的开源工具，支持作为独立的反向代理或集成到现有基础设施中的中间件，通过 OAuth2/OIDC 认证保护 Web 应用。其核心功能包括：

1. **认证支持**  
   支持多种 OAuth2/OIDC 提供者（如 Google、Microsoft Entra ID、GitHub 等），并能提取用户信息（如用户名、组别），通过 HTTP 头转发至上游应用。

2. **部署方式**  
   提供编译二进制文件（支持主流架构及特殊架构如 ppc64le、s390x）和 Docker 镜像。从 v7.6.0 版本起，默认使用安全性更高的 [GoogleContainerTools/distroless](https://github.com/GoogleContainerTools/distroless) 镜像，并提供夜间构建版本（`quay.io/oauth2-proxy/oauth2-proxy-nightly`）。

3. **社区与贡献**  
   鼓励社区参与，提供 Slack 频道（`#oauth2-proxy`）和详细的 [贡献指南](https://oauth2-proxy.github.io/oauth2-proxy/community/contribution)。项目由众多贡献者维护，支持通过 PR 添加用户案例。

4. **安全与版本管理**  
   建议升级至 v6.0.0 及以上版本以修复安全漏洞（如开放重定向漏洞）。提供安全披露流程，确保漏洞处理的私密性。

5. **许可证**  
   采用 MIT 开源许可证，允许自由使用和分发。

该工具适用于需要通过 OAuth2/OIDC 认证保护 Web 应用的场景，兼顾灵活性与安全性，适合企业级部署和开发需求。