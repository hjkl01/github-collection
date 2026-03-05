
---
title: edgevpn
---

### [mudler edgevpn](https://github.com/mudler/edgevpn)  ![GitHub Repo stars](https://img.shields.io/github/stars/mudler/edgevpn?style=social)

EdgeVPN 是一个基于 libp2p 的完全去中心化私有网络工具，无需中央服务器，通过共享密钥连接节点。核心功能包括：
1. **VPN**：在 P2P 节点间建立安全网络，支持自动分配 IP 和内置 DNS。
2. **反向代理**：无需建立 VPN 即可将 TCP 服务暴露到 P2P 网络。
3. **文件传输**：支持节点间 P2P 安全传输文件。
4. **库支持**：可作为 Go 库集成，提供分布式账本功能。
适用于边缘设备和开发环境（如 Kubernetes 集群），不适用于生产环境或低延迟场景，且尚未经过完整安全审计。