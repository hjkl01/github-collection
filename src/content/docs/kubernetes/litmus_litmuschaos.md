
---
title: litmus
---

### [litmuschaos litmus](https://github.com/litmuschaos/litmus)  ![GitHub Repo stars](https://img.shields.io/github/stars/litmuschaos/litmus?style=social)

LitmusChaos 是一个云原生的开源混沌工程平台（CNCF 项目），旨在通过受控方式在基础设施中注入混沌测试，以识别潜在弱点及故障。该平台基于 Kubernetes 自定义资源（CRs）实现混沌的创建、管理和监控。核心架构包含混沌控制平面（用于编排、调度与可视化）和执行平面（负责实验执行与监控）。主要资源包括 ChaosExperiment（定义故障模板）、ChaosEngine（关联应用与配置探针）和 ChaosResult（记录结果与指标），支持通过 Workflow 编排实验。适用场景包括开发人员扩展测试、CI/CD 流水线故障检测以及 SRE 提升系统韧性。平台提供中央实验库共享混沌模板，并支持集成第三方工具。