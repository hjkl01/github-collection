
---
title: tyk
---

### [TykTechnologies tyk](https://github.com/TykTechnologies/tyk)  ![GitHub Repo stars](https://img.shields.io/github/stars/TykTechnologies/tyk?style=social)

Tyk API Gateway 是一款云原生、开源且适用于企业级的 API 网关，支持 REST、GraphQL、gRPC、TCP 和 SOAP 协议。其核心功能包括：

1. **安全认证**：内置支持 OIDC、JWT、Bearer Token、Basic Auth 及客户端证书，提供 IP 白/黑名单、CORS 及细粒度访问控制。
2. **流量治理**：具备限流、配额管理、API 版本控制及速率限制能力，防止上游服务过载。
3. **内容中介**：支持请求/响应头转换及格式转换（如 SOAP 与 GraphQL 互转）。
4. **高性能与扩展**：低延迟、高吞吐，支持水平/垂直扩展及 Kubernetes 原生部署（通过 Operator）。
5. **可观测性与插件**：提供详细 API 使用日志、Webhooks 事件通知，支持通过 Go、Python、JS 等语言编写自定义插件。
6. **配置管理**：支持配置热重载，无需中断活跃请求即可更新服务。

项目采用 MPL 2.0 开源许可，核心功能免费，部分企业级功能（位于 'ee' 文件夹）需商业授权。