
---
title: litmus
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/litmuschaos/litmus?style=social) ](https://github.com/litmuschaos/litmus)
### [litmuschaos litmus](https://github.com/litmuschaos/litmus)

**LitmusChaos 核心内容总结：**

**项目功能**  
LitmusChaos 是一款面向 Kubernetes 的混沌工程工具，用于模拟故障（如网络延迟、节点宕机、磁盘故障等），以验证系统弹性和生产就绪性。支持通过自定义资源定义（CRD）管理混沌实验，提供控制平面、指标收集与可视化功能，可集成 Argo Workflows 实现复杂工作流编排。

**使用方法**  
用户通过 YAML 文件定义混沌实验场景，使用 `kubectl` 命令行工具进行实验创建、监控与终止。官方文档（[Litmus Docs](https://docs.litmuschaos.io)）提供详细操作指南。

**主要特性**  
1. **基于 Kubernetes CRD**：所有实验配置通过 Kubernetes 原生资源管理，无需额外依赖。  
2. **多故障类型支持**：涵盖网络、存储、计算等常见故障注入，支持自定义插件扩展。  
3. **可视化与监控**：集成 Prometheus 等工具，提供实验状态追踪与指标分析。  
4. **安全与可控**：通过命名空间隔离、实验范围限制等机制保障测试安全。  
5. **CNCF 生态兼容**：作为 CNCF 孵化项目，与 Kubernetes、Argo 等工具深度集成。