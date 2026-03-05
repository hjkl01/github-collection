
---
title: kwok
---

### [kubernetes-sigs kwok](https://github.com/kubernetes-sigs/kwok)  ![GitHub Repo stars](https://img.shields.io/github/stars/kubernetes-sigs/kwok?style=social)

KWOK（Kubernetes WithOut Kubelet）是一个轻量级工具包，能够在秒级时间内于本地搭建包含数千个模拟节点的 Kubernetes 集群。核心组件 kwok 负责模拟节点、Pod 及 API 资源的生命周期，CLI 工具 kwokctl 用于集群管理。该工具资源消耗低、运行速度快，兼容 kubectl 等标准 Kubernetes 客户端，支持灵活配置节点属性与 Pod 行为，适用于测试不同场景及边缘案例。