
---
title: k3s
---

### [k3s-io k3s](https://github.com/k3s-io/k3s)  ![GitHub Repo stars](https://img.shields.io/github/stars/k3s-io/k3s?style=social)

K3s 是一个轻量级、生产就绪的 Kubernetes 发行版。采用小于 100 MB 的单一二进制文件部署，内存占用减半，且完全符合 Kubernetes 标准。K3s 默认支持 SQLite3 存储（也支持 Etcd3、MySQL 等），集成了容器运行时、网络、DNS、负载均衡及监控组件，简化了运维操作。为减小体积，它移除了内嵌存储驱动和云提供者，且无需在 Worker 节点暴露 kubelet 端口。适用于边缘计算、物联网、CI、开发及 ARM 等场景，跟随上游版本发布，支持脚本快速安装。