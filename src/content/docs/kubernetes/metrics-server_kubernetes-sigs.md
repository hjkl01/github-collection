
---
title: metrics-server
---

### [kubernetes-sigs metrics-server](https://github.com/kubernetes-sigs/metrics-server)  ![GitHub Repo stars](https://img.shields.io/github/stars/kubernetes-sigs/metrics-server?style=social)

Kubernetes Metrics Server 是一个可扩展、高效的 Kubernetes 容器资源指标收集组件，专为内置自动伸缩管道设计。它从 Kubelet 收集资源指标并通过 Metrics API 暴露给 apiserver，主要供 Horizontal Pod Autoscaler、Vertical Pod Autoscaler 及 `kubectl top` 命令使用。该组件每 15 秒收集一次指标，资源占用低（每节点约 1m CPU 和 2MB 内存），支持高达 5000 节点的集群规模。需注意，Metrics Server 仅用于自动扩容目的，不可作为监控解决方案的指标源或提供精确的资源使用数据，其他监控需求应使用 Prometheus 等完整监控方案。