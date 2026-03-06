
---
title: k3s
---

### [k3s-io k3s](https://github.com/k3s-io/k3s)  ![GitHub Repo stars](https://img.shields.io/github/stars/k3s-io/k3s?style=social)

K3s 是一款轻量级、生产就绪的 Kubernetes 发行版。其主要功能包括：打包为单一二进制文件（小于 100 MB），内存占用减半，易于安装且最小化 OS 依赖；适用于边缘计算、物联网、CI、开发及 ARM 场景；内置 Containerd、Flannel、CoreDNS、Traefik 等组件，默认使用 SQLite3 存储（支持 etcd 等）；自动管理 TLS 证书和节点连接，通过隧道优化 kubelet 暴露；保持与上游 Kubernetes 高度兼容，移除 In-tree 存储驱动和云提供程序以保持轻量化。