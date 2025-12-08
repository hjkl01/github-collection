
---
title: KAI-Scheduler
---

### [NVIDIA KAI-Scheduler](https://github.com/NVIDIA/KAI-Scheduler)

**项目核心内容总结：**

**功能**  
KAI Scheduler 是一个 Kubernetes 调度器，专注于优化 GPU 资源分配，适用于 AI 和机器学习工作负载，支持大规模 GPU 集群管理，可动态分配资源并确保不同用户间的公平性，兼容其他调度器。

**使用方法**  
1. **前提条件**：需 Kubernetes 集群、Helm CLI 及 NVIDIA GPU-Operator。  
2. **安装**：  
   - **推荐方式**：通过 Helm 安装，命名空间为 `kai-scheduler`，需替换版本号。  
   - **源码构建**：参考文档 `docs/developer/building-from-source.md`。  
   - **OpenShift 特殊说明**：若 GPU-Operator 版本低于 v25.10.0，需添加 `--set admission.gpuPodRuntimeClassName=null` 参数。  

**主要特性**  
- 批量调度、装箱/分散调度、工作负载优先级、分层队列管理。  
- 资源分配与公平策略（如 DRF 算法、资源回收）。  
- 支持弹性工作负载、动态资源分配（DRA）、GPU 共享。  
- 适配云环境（如 Karpenter）及本地部署。  
- 提供工作负载整合、最小/最大 Pod 数量限制等功能。  

**注意事项**  
- 提交工作负载时需使用独立命名空间，不可使用 `kai-scheduler` 命名空间。  
- 安装前需确认 GPU-Operator 版本兼容性。