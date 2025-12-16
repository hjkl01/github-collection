
---
title: quic-go
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/quic-go/quic-go?style=social) ](https://github.com/quic-go/quic-go)
### [quic-go quic-go](https://github.com/quic-go/quic-go)

**核心内容总结：**  
quic-go 是一个用 Go 语言实现的 QUIC 协议库，支持 HTTP/3（含 QPACK 和 HTTP Datagrams）及多个 RFC 标准（如 DPLPMTUD、QUIC Version 2 等）。主要特性包括：  
1. **协议支持**：实现 QUIC 协议（RFC 9000/9001/9002）、HTTP/3（RFC 9114）及扩展功能（如不可靠数据报、路径 MTU 发现）。  
2. **兼容性**：支持最新两个 Go 版本，提供详细的文档和测试覆盖率。  
3. **生态集成**：支持 WebTransport over HTTP/3（通过 webtransport-go 项目）。  
4. **应用案例**：被 AdGuardHome、Caddy、Cloudflare 等多个知名项目采用。  

**使用方法**：作为 Go 库集成到项目中，用于构建基于 QUIC 和 HTTP/3 的网络应用。