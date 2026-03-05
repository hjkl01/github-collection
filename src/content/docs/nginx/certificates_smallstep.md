
---
title: certificates
---

### [smallstep certificates](https://github.com/smallstep/certificates)  ![GitHub Repo stars](https://img.shields.io/github/stars/smallstep/certificates?style=social)

`step-ca` 是一个面向 DevOps 的在线证书颁发机构（CA）及私钥基础设施（PKI）工具，核心功能如下：

1. **证书签发**：支持颁发符合标准的 HTTPS/TLS 证书（兼容浏览器）及 SSH 证书，适用于服务器、容器、数据库连接及 Kubernetes 等环境。
2. **自动化管理**：内置 ACME 服务器，支持 HTTP-01、DNS-01 等多种挑战类型，兼容主流 ACME 客户端；支持通过 OAuth OIDC 令牌、云实例身份文档、JWK 令牌等多种方式授权证书颁发。
3. **SSH 集成**：支持 SSH 证书替代传统公钥认证，可对接 SSO 提供商实现短生命周期证书及多因素认证，支持主机证书的自动续期。
4. **灵活配置**：支持多种密钥类型（RSA、ECDSA、EdDSA）及数据库后端（PostgreSQL、MySQL、Badger 等），可作为现有根 CA 的中间 CA 运行。
5. **工具链协同**：与 `step` CLI 工具配合，实现密钥生成、证书续期、吊销、根证书安装及 PKI 信任链建立。