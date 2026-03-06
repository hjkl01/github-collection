
---
title: kwok
---

### [kubernetes-sigs kwok](https://github.com/kubernetes-sigs/kwok)  ![GitHub Repo stars](https://img.shields.io/github/stars/kubernetes-sigs/kwok?style=social)

KWOK (Kubernetes WithOut Kubelet) 是一个 Kubernetes 工具包，旨在几秒钟内模拟部署数千个节点的集群。它包含两个核心组件：`kwok` 负责模拟虚假节点、Pod 及其他 Kubernetes API 资源的生命周期；`kwokctl` 是用于创建和管理基于模拟节点集群的 CLI 工具。项目主要特点包括：轻量级，可在笔记本低资源消耗下模拟大规模节点和 Pod；快速，支持秒级创建和删除集群及节点；兼容性，适配 kubectl、helm 等 Kubernetes 标准工具；可移植性，支持 Docker、Nerdctl 或二进制运行；灵活性，可自定义节点属性及 Pod 行为以测试不同场景。