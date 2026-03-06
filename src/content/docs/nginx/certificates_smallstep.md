
---
title: certificates
---

### [smallstep certificates](https://github.com/smallstep/certificates)  ![GitHub Repo stars](https://img.shields.io/github/stars/smallstep/certificates?style=social)

`step-ca` 是一个面向 DevOps 的在线证书颁发机构（CA），提供安全、自动化的证书管理服务，作为 `step` CLI 工具的服务器端。核心功能包括：

1.  **多类型证书签发**：支持颁发 HTTPS 服务器/客户端证书、DevOps 环境 TLS 证书（VM、容器、数据库、K8s 等）及 SSH 证书（支持用户通过 SSO、主机通过云实例身份认证）。
2.  **自动化管理**：内置 ACME 服务器，支持多种挑战类型（http-01, dns-01, tls-alpn-01 等）；支持通过 OAuth OIDC、云实例身份文档、JWK、X5C 等多种方式建立信任链并授权签发。
3.  **灵活 PKI 能力**：支持 RSA、ECDSA、EdDSA 等多种密钥类型，支持短生命周期证书的自动续期与被动吊销，支持多种数据库后端，可配置为现有根 CA 的中间 CA。
4.  **工具深度集成**：通过 `step` CLI 配合使用，支持私钥在本地生成、根证书分发、证书安装、检查、续期和吊销，确保私钥不跨网络传输。