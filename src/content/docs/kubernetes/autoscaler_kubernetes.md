
---
title: autoscaler
---

### [kubernetes autoscaler](https://github.com/kubernetes/autoscaler)  ![GitHub Repo stars](https://img.shields.io/github/stars/kubernetes/autoscaler?style=social)

该项目包含 Kubernetes 自动扩缩相关组件，核心功能如下：

1. **集群自动扩缩器**：自动调整 Kubernetes 集群的节点规模，确保所有 Pod 可运行且无闲置节点，支持多家公有云。
2. **垂直自动扩缩器**：自动调整运行在集群中的 Pod 所请求的 CPU 和内存资源量。
3. **Addon Resizer**：基于集群节点数量修改部署资源请求量的简化版自动扩缩器。

此外，项目还提供上述组件的官方 Helm Chart。