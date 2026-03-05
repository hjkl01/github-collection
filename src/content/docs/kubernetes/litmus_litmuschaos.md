
---
title: litmus
---

### [litmuschaos litmus](https://github.com/litmuschaos/litmus)  ![GitHub Repo stars](https://img.shields.io/github/stars/litmuschaos/litmus?style=social)

LitmusChaos 是一款基于 Kubernetes 的开源混沌工程平台（CNCF 项目），旨在通过受控方式注入故障测试，帮助团队识别基础设施中的弱点及潜在故障，从而提升系统韧性。

核心功能包括：
1. **云原生架构**：由混沌控制平面（集中管理、调度、可视化）和混沌执行平面（代理及算子负责实验执行与监控）组成。
2. **Kubernetes 集成**：利用自定义资源（CRs）定义混沌流程，包括 ChaosExperiment（故障配置模板）、ChaosEngine（关联工作负载与稳态验证）、ChaosResult（实验结果与 Prometheus 指标）。
3. **多场景支持**：适用于开发人员集成测试、CI/CD 管道阶段验证以及 SRE 故障演练规划。
4. **扩展性**：提供中央实验枢纽共享资源，支持 BYOC（Bring Your Own Chaos）以集成第三方工具。