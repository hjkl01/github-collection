### [coredns coredns](https://github.com/coredns/coredns)  ![GitHub Repo stars](https://img.shields.io/github/stars/coredns/coredns?style=social)

CoreDNS 是由 Go 语言编写的高性能、灵活的 DNS 服务器和转发器，属于 CNCF 毕业项目。采用插件化架构，通过 Corefile 配置文件组合插件实现定制化功能。

主要功能包括：
1. **多协议支持**：兼容 UDP/TCP、DNS over TLS (DoT)、DNS over HTTP/2/3 (DoH)、QUIC (DoQ) 及 gRPC。
2. **DNS 服务**：支持区域文件解析、DNSSEC 签名与验证、区域传输、缓存及自动加载。
3. **查询处理**：支持转发查询至递归服务器、DNS64 IPv6 转换及查询重写。
4. **后端集成**：可对接 etcd、Kubernetes 及云服务商（如 Route53）作为数据源。
5. **运维监控**：提供 Prometheus 指标暴露、查询日志记录及错误追踪。