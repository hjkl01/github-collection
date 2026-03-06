
---
title: iroh
---

### [n0-computer iroh](https://github.com/n0-computer/iroh)  ![GitHub Repo stars](https://img.shields.io/github/stars/n0-computer/iroh?style=social)

Iroh 是一个基于 Rust 的网络通信库，提供通过公钥建立连接的 API，能够自动发现并维护到目标设备的最快路径。它优先尝试 NAT 穿透建立直连，失败则自动回退到公共中继服务器，并通过持续测量优化性能。底层采用 QUIC 协议，内置认证加密、并发流及避免队头阻塞等特性。此外，项目还提供一系列构建在其上的协议库，包括用于内容寻址数据传输的 iroh-blobs、用于发布订阅网络的 iroh-gossip、用于最终一致性键值存储的 iroh-docs 以及 Willow 协议实现。支持 Rust 原生开发及通过 FFI 供其他语言使用。