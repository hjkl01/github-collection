
---
title: autoscaler
---

### [kubernetes autoscaler](https://github.com/kubernetes/autoscaler)  ![GitHub Repo stars](https://img.shields.io/github/stars/kubernetes/autoscaler?style=social)

本项目提供 Kubernetes 的自动扩展组件，核心功能包括：
1. Cluster Autoscaler：自动调整集群节点规模，确保 Pod 有运行位置且无多余节点，支持公有云（GA 版本）。
2. Vertical Pod Autoscaler：自动调整运行中 Pod 的 CPU 和内存资源请求（Beta 版本）。
3. Addon Resizer：根据节点数量简化调整资源请求（Beta 版本）。
此外还提供各组件对应的 Helm Chart 支持。