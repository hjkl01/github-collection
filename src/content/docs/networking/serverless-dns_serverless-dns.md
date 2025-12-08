
---
title: serverless-dns
---

### [serverless-dns serverless-dns](https://github.com/serverless-dns/serverless-dns)

**项目核心内容总结：**

**1. 项目功能**  
`serverless-dns` 是一个支持多平台部署的 DNS 解析工具，提供以下核心功能：  
- 支持 DNS over HTTPS (DoH)、DNS over TCP 等协议；  
- 集成 200+ 块列表（如恶意域名、广告域名等），通过压缩的 **Succinct Radix Trie** 实现高效查询；  
- 支持缓存机制（LFU 缓存、Cloudflare Cache API）提升解析效率；  
- 提供 TLS 终止、PSK 加密、域名伪装（Domain Fronting）等安全特性；  
- 支持自定义 DNS 上游解析器（如 Cloudflare、1.1.1.1 等）。  

**2. 使用方法**  
- **部署方式**：  
  - **Cloudflare Workers**：通过 `wrangler publish` 发布；  
  - **Fastly Compute@Edge**：使用 `fastly compute publish` 部署；  
  - **Fly.io**：通过 `flyctl deploy` 部署，需配置 `fly.toml`；  
  - **本地运行**：需设置 TLS 证书路径（`TLS_KEY_PATH`、`TLS_CRT_PATH`）。  
- **配置**：  
  - 通过环境变量（如 `CF_DNS_RESOLVER_URL`、`TLS_PSK`）自定义 DNS 上游、安全策略等。  

**3. 主要特性**  
- **多平台兼容**：支持 Node.js、Deno Deploy、Cloudflare Workers、Fastly Compute@Edge、Fly.io 等运行时；  
- **高效块列表管理**：块列表每日更新，压缩存储，提升查询速度；  
- **灵活的安全配置**：支持 TLS/PSK、域名伪装、自定义证书；  
- **缓存优化**：根据平台使用 LFU 缓存或 Cloudflare 内置缓存；  
- **分析接口**：提供客户端 IP、查询域名、区域等统计信息（通过 `max.rethinkdns.com` 接口）。  

**适用场景**：适用于需要高性能、安全的 DNS 解析服务，尤其适合云原生、无服务器架构的部署需求。