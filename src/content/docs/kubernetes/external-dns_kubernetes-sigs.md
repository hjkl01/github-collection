
---
title: external-dns
---

### [kubernetes-sigs external-dns](https://github.com/kubernetes-sigs/external-dns)  ![GitHub Repo stars](https://img.shields.io/github/stars/kubernetes-sigs/external-dns?style=social)

ExternalDNS 是一个 Kubernetes 项目，旨在同步暴露的 Kubernetes Services 和 Ingresses 至外部 DNS 提供商，使集群资源可通过公共 DNS 发现。它通过监听 Kubernetes API 获取资源信息，自动管理 DNS 记录的创建与更新，而非自身作为 DNS 服务器。项目支持 AWS Route 53、Google Cloud DNS 等多种 DNS 服务商，利用 TXT 记录确保对托管区域的安全管理。ExternalDNS 支持通过注解动态控制 DNS，提供集群部署和本地运行模式，并允许通过 Webhook 系统扩展新的 DNS 提供商支持。