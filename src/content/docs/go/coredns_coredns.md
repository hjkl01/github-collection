
---
title: coredns
---

### [coredns coredns](https://github.com/coredns/coredns)

**CoreDNS 核心内容总结：**

CoreDNS 是一个用 Go 编写的高性能、可扩展的 DNS 服务器/转发器，支持通过插件链式组合实现灵活的 DNS 功能。其核心特性包括：  
- **功能**：支持 DNSSEC、负载均衡、缓存、区域传输（AXFR）、动态后端（etcd/k8s）、查询转发、日志记录、云服务商集成（如 Route53）等；支持多种协议（DoT/DoH/DoQ/QUIC/gRPC）。  
- **使用方法**：通过 `Corefile` 配置文件定义监听端口、插件及规则，支持导入外部文件、使用环境变量。编译需 Go 1.24+，可直接源码构建或通过 Docker 容器生成二进制文件。  
- **扩展性**：基于插件系统，用户可自定义功能（如通过 `rewrite` 插件修改查询内容），或使用社区提供的扩展插件（ExPlugins）。  

**主要优势**：轻量、高性能、协议兼容性强，适用于云原生环境及复杂 DNS 管理场景。