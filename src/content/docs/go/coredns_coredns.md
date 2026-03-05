
---
title: coredns
---

### [coredns coredns](https://github.com/coredns/coredns)  ![GitHub Repo stars](https://img.shields.io/github/stars/coredns/coredns?style=social)

CoreDNS 是一个基于 Go 开发的高性能、灵活可扩展的 DNS 服务器与转发器，隶属于云原生计算基金会（CNCF）毕业项目。采用插件化架构，支持通过插件组合实现多种 DNS 功能。支持 UDP/TCP、TLS (DoT)、HTTP/2 (DoH)、HTTP/3 (DoH3)、QUIC (DoQ) 及 gRPC 等多种传输协议。核心功能包括：从文件自动加载区域数据（支持 DNSSEC）、区域传输（主/从服务器）、DNS 响应缓存、负载均衡、上游代理转发、集成 Kubernetes 和 etcd 后端、提供指标与日志、云服务商集成、查询重写、阻止 ANY 查询及 DNS64 IPv6 转换等。系统配置通过 Corefile 文件定义。