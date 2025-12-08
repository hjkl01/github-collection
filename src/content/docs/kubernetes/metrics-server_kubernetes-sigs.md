
---
title: metrics-server
---

### [kubernetes-sigs metrics-server](https://github.com/kubernetes-sigs/metrics-server)

### 核心内容总结  

**项目功能**  
Kubernetes Metrics Server 是 Kubernetes 自动扩展（HPA、VPA）的资源指标来源，通过 Metrics API 提供 CPU/内存使用数据，支持 `kubectl top` 命令调试自动扩展。  

**主要特性**  
- **高效性**：每 15 秒收集一次指标，资源占用低（每个节点约 1m CPU、2MB 内存）。  
- **兼容性**：支持最多 5000 节点集群，适配主流 Kubernetes 版本（1.8+）。  
- **安全性**：需启用 kube-apiserver 聚合层、Kubelet 身份验证，且不支持非 Kubernetes 集群或监控场景。  

**使用方法**  
- **安装**：通过 YAML 文件或 Helm Chart 部署，命令示例：  
  ```bash  
  kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml  
  ```  
- **高可用**：通过设置 `replicas > 1` 实现，需 kube-apiserver 启用 `--enable-aggregator-routing=true`。  

**注意事项**  
- 不适用于监控场景，需直接从 Kubelet `/metrics/resource` 获取指标。  
- 安装前需确保集群满足网络、证书、聚合层等要求。  
- 资源配额需根据集群规模调整（如节点数超过 100，需额外分配 1m CPU/2MB 内存）。  

**兼容性**  
不同 Metrics Server 版本支持的 Kubernetes 版本及 Metrics API 版本不同，需按兼容性矩阵匹配。  

**设计**  
通过 Metrics API 提供数据，依赖 Pod/Node Informer 获取信息，缓存后返回给 kube-apiserver。