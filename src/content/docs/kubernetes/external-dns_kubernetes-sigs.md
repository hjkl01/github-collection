
---
title: external-dns
---

### [kubernetes-sigs external-dns](https://github.com/kubernetes-sigs/external-dns)  ![GitHub Repo stars](https://img.shields.io/github/stars/kubernetes-sigs/external-dns?style=social)

ExternalDNS 是一个将 Kubernetes 服务（Service）和 Ingress 资源与外部 DNS 提供商同步的工具。它通过监控 Kubernetes API 中的资源，动态管理对应的 DNS 记录，配置外部 DNS 服务提供商（如 AWS Route 53、Google Cloud DNS、Azure DNS 等），而非自身充当 DNS 服务器。该工具支持以无厂商依赖的方式通过 Kubernetes 资源控制 DNS 记录，具备 TXT 记录所有权跟踪以安全维护托管区域，支持干跑模式，并可通过 Webhook 系统扩展支持更多 DNS 服务。