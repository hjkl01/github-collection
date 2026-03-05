
---
title: KAI-Scheduler
---

### [NVIDIA KAI-Scheduler](https://github.com/NVIDIA/KAI-Scheduler)  ![GitHub Repo stars](https://img.shields.io/github/stars/NVIDIA/KAI-Scheduler?style=social)

KAI Scheduler 是一个基于 Kubernetes 的鲁棒、高效且可扩展的调度器，专为 AI 和机器学习工作负载优化 GPU 资源分配。它适用于管理包含数千节点的大规模 GPU 集群及高吞吐工作负载。

核心功能包括：
1. **智能调度**：支持批量调度（Gang Scheduling）、拓扑感知调度（TAS）及分层 Pod 组，优化分布式与异构架构工作负载的放置。
2. **资源管理**：提供装箱与分散调度、分层队列、基于时间的公平分享、DRF 公平性策略及资源抢占策略分离。
3. **高级特性**：涵盖动态资源分配（DRA）、GPU 共享、弹性工作负载、运行中工作负载重组及调度过程可解释性日志。
4. **兼容性**：基于 kube-batch 构建，兼容云端与本地部署，可与其他调度器共存于同一集群。