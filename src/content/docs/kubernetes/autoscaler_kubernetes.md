
---
title: autoscaler
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/kubernetes/autoscaler?style=social) ](https://github.com/kubernetes/autoscaler)
### [kubernetes autoscaler](https://github.com/kubernetes/autoscaler)

**项目核心内容总结：**  
Kubernetes Autoscaler 是一组用于 Kubernetes 集群自动扩展的组件，包含以下功能模块：  

1. **Cluster Autoscaler（集群自动扩展器）**  
   - 自动调整 Kubernetes 集群规模，确保所有 Pod 有运行空间并避免冗余节点。  
   - 支持主流公有云提供商，版本 1.0 已稳定发布（GA）。  
   - 提供对应的 Helm Chart 用于部署。  

2. **Vertical Pod Autoscaler（垂直 Pod 自动扩展器）**  
   - 自动优化 Pod 的 CPU 和内存请求值，提升资源利用率。  
   - 当前处于 Beta 阶段，提供 Helm Chart 部署支持。  

3. **Addon Resizer（附加组件调整器）**  
   - 根据集群节点数量自动调整特定 Deployment 的资源请求值。  
   - 当前为 Beta 版本，功能简化，适用于特定场景。  

**使用方法：**  
- 通过 GitHub Fork 项目，使用 Git 将代码克隆到 `$GOPATH/src/k8s.io` 目录下（需替换个人 GitHub 用户名）。  
- 各组件可通过 Helm Chart 部署。  

**主要特性：**  
- 支持多云平台（Cluster Autoscaler）。  
- 提供资源优化（Vertical Pod Autoscaler）与简化调整（Addon Resizer）。  
- 各模块均提供 Helm 部署方案，便于集成到 Kubernetes 生态。