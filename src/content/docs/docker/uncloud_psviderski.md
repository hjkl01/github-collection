
---
title: uncloud
---

### [psviderski uncloud](https://github.com/psviderski/uncloud)  ![GitHub Repo stars](https://img.shields.io/github/stars/psviderski/uncloud?style=social)

Uncloud 是一个轻量级的容器集群编排工具，旨在让用户在不使用 Kubernetes 或 Swarm 复杂架构的情况下，在多台服务器（包括云虚拟机、专用服务器和裸机）上部署和管理容器化应用。

主要功能：
1. **跨平台统一环境**：支持混合使用不同提供商的云资源和本地硬件，整合为统一计算环境。
2. **Docker Compose 兼容**：使用熟悉的 Docker Compose 格式定义服务，无需学习新语言。
3. **零配置私有网络**：自动构建 WireGuard mesh 网络，实现容器间的跨机器直接通信。
4. **自动 HTTPS 与 DNS**：内置 Caddy 反向代理和 Managed DNS 服务，自动处理域名解析和 TLS 证书。
5. **去中心化架构**：无中央控制平面，节点通过 P2P 通信同步状态，降低运维复杂度并避免单点故障。
6. **服务生命周期管理**：支持滚动更新、零停机部署、服务发现、负载均衡及持久化存储。
7. **简单 CLI 控制**：提供类 Docker 的命令管理基础设施，支持通过 SSH 远程管理集群。