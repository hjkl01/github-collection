
---
title: edgevpn
---

### [mudler edgevpn](https://github.com/mudler/edgevpn)  ![GitHub Repo stars](https://img.shields.io/github/stars/mudler/edgevpn?style=social)

EdgeVPN 是一个基于 libp2p 技术构建的去中心化私有网络工具，通过共享密钥实现无需中心服务器的节点连接。核心功能如下：
1. **安全 VPN**：在 P2P 节点间建立加密隧道，支持自动分配 IP 和嵌入式 DNS。
2. **反向代理**：无需建立 VPN 即可通过 P2P 隧道暴露本地 TCP 服务。
3. **P2P 文件传输**：支持节点间直接传输文件。
4. **库功能**：可作为 Go 库集成，提供分布式账本接口。
项目提供静态编译版本及命令行/GUI 界面，适用于边缘设备、Kubernetes 集群及开发环境网络搭建。