
---
title: metrics-server
---

### [kubernetes-sigs metrics-server](https://github.com/kubernetes-sigs/metrics-server)  ![GitHub Repo stars](https://img.shields.io/github/stars/kubernetes-sigs/metrics-server?style=social)

Kubernetes Metrics Server 是为 Kubernetes 内置自动扩缩容管道设计的容器资源指标收集服务。它从 Kubelet 采集 CPU 和内存指标，通过 Metrics API 暴露给 API Server，供 Horizontal Pod Autoscaler (HPA)、Vertical Pod Autoscaler (VPA) 及 `kubectl top` 命令使用。

该项目专用于基于 CPU/内存的自动扩缩容和资源建议，不应用于通用监控场景。其特点为资源效率高（每节点约 1m CPU、2MB 内存），支持高可用部署，可扩展至 5000 节点集群。支持通过 YAML 清单或 Helm Chart 进行安装和配置。