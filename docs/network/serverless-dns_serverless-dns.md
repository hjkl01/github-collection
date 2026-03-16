### [serverless-dns serverless-dns](https://github.com/serverless-dns/serverless-dns)  ![GitHub Repo stars](https://img.shields.io/github/stars/serverless-dns/serverless-dns?style=social)

serverless-dns 是一款自托管的、类似 Pi-hole 的内容拦截型 DNS 解析器，支持 DNS-over-HTTPS (DoH) 和 DNS-over-TLS (DoT) 协议。它专为边缘计算设计，可部署在 Cloudflare Workers、Deno Deploy、Fastly Compute@Edge 和 Fly.io 等平台上。

主要功能特性：
1. **内容拦截**：整合 200 多个黑名单源，编译约 1700 万条规则，采用压缩 Radix Trie 结构提升查询效率。
2. **高性能解析**：服务器端处理延迟 0-2ms，端到端延迟通常在 10-30ms 之间。
3. **安全认证**：支持通过 Bearer Token 对 DoH 和 DoT 进行认证，并提供 TLS PSK 加密套件支持。
4. **日志与分析**：支持将日志推送到 Cloudflare R2，并提供按域名、IP、地区等维度的 DNS 分析数据。
5. **灵活配置**：允许通过环境变量和网页界面自定义黑名单及解析策略，免费套餐足以覆盖 10-20 台设备。