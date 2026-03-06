
---
title: uncloud
---

### [psviderski uncloud](https://github.com/psviderski/uncloud)  ![GitHub Repo stars](https://img.shields.io/github/stars/psviderski/uncloud?style=social)

Uncloud 是一款轻量级容器编排工具，允许开发者在云服务器和裸金属服务器上部署和扩展容器化应用，无需 Kubernetes 或 Swarm 的复杂开销。其核心功能包括：

1.  **去中心化架构**：无中心控制平面，节点通过 P2P 通信同步集群状态，保证部分节点离线时服务仍可用。
2.  **自动化网络**：自动构建 WireGuard 网格网络，提供内置 DNS、负载均衡、HTTPS 自动证书及跨机器通信。
3.  **便捷部署**：支持 Docker Compose 格式，提供类 Docker CLI 命令，支持本地镜像传输、持久化存储及零停机滚动更新。
4.  **远程管理**：可通过 SSH 或 CLI 控制集群，每个节点均可独立管理整个集群状态。

该项目旨在为开发者提供灵活且易于维护的自托管基础设施体验。