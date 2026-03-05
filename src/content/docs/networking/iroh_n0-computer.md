
---
title: iroh
---

### [n0-computer iroh](https://github.com/n0-computer/iroh)  ![GitHub Repo stars](https://img.shields.io/github/stars/n0-computer/iroh?style=social)

Iroh 是一个基于 Rust 的网络库，提供基于公钥拨号的 API，可自动寻找并维持设备间的最优连接。它支持 NAT 穿透，直连优先，失败则使用公共中继服务器。底层基于 QUIC 协议，内置认证加密、并发流及避免队头阻塞等特性。项目包含内容寻址传输（iroh-blobs）、发布订阅网络（iroh-gossip）及最终一致性键值存储（iroh-docs）等预构建协议组件。支持 Rust 原生使用，并提供 FFI 绑定以兼容其他语言。