
---
title: certificates
---

### [smallstep certificates](https://github.com/smallstep/certificates)

### 项目核心内容总结

**项目功能**  
`step-ca` 是一个用于 DevOps 的在线证书颁发机构（CA），支持 HTTPS/TLS/SSH 证书的自动化管理。主要功能包括：  
- 发行符合浏览器和 RFC5280 标准的 HTTPS 证书  
- 为虚拟机、容器、数据库等 DevOps 场景发行 TLS 证书  
- 发行 SSH 证书（支持用户身份验证和云主机身份绑定）  
- 作为 ACME 服务器支持自动 HTTPS 证书签发  
- 提供命令行工具 `step` 实现证书生成、续订、吊销等操作  

**使用方法**  
- 通过 ACME 协议与客户端（如 Certbot、Caddy、Traefik）集成  
- 使用 OAuth OIDC 令牌（如 Okta、Keycloak）或云实例文档（AWS/GCP/Azure）授权证书签发  
- 通过 `step` CLI 工具实现证书管理（生成、安装、验证等）  
- 支持多种数据库后端（Badger、BoltDB、PostgreSQL、MySQL）  

**主要特性**  
1. **灵活的 PKI 管理**  
   - 支持 RSA/ECDSA/EdDSA 密钥类型及自定义证书生命周期  
   - 可作为现有根 CA 的中间 CA 运行  
   - 短生命周期证书自动续订与被动吊销机制  

2. **多场景自动化**  
   - 支持 ACME 挑战类型（HTTP-01、DNS-01、TLS-ALPN-01）  
   - 集成 OAuth OIDC、云实例文档、JWK 令牌等多种授权方式  
   - 提供 Go 库和 CLI 工具简化开发集成  

3. **SSH 证书管理**  
   - 替代传统 `authorized_keys` 文件，支持基于 SSO 的动态 SSH 用户证书  
   - 自动化主机证书续订，消除 SSH TOFU 警告  

4. **开发友好**  
   - 提供 ACME 服务器、数据库配置、多语言客户端示例（Go/Python/Node.js）  
   - 支持通过 `step` CLI 实现零网络传输的密钥生成与证书申请