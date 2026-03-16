### [NVIDIA KAI-Scheduler](https://github.com/NVIDIA/KAI-Scheduler)  ![GitHub Repo stars](https://img.shields.io/github/stars/NVIDIA/KAI-Scheduler?style=social)

KAI Scheduler 是一个基于 Kubernetes 的鲁棒、高效且可扩展的调度器，专为优化 AI 和机器学习工作负载的 GPU 资源分配而设计，适用于大规模 GPU 集群。

核心功能包括：
1. **大规模与高吞吐管理**：支持数千节点及高吞吐工作负载，完全兼容云和本地部署环境。
2. **调度与资源优化**：提供批调度（Gang Scheduling）、资源打包与分散调度、弹性工作负载动态扩缩容及工作负载签名优化。
3. **公平性与队列控制**：支持层级队列、主导资源公平性（DRF）、时间公平性调度，以及优先级与抢占性分离策略。
4. **拓扑与硬件感知**：具备拓扑感知调度（TAS）以优化分离式架构，支持动态资源分配（DRA）及 NVIDIA/AMD GPU 共享。
5. **集成与可解释性**：原生集成 KubeRay，基于 K8S Events 记录调度步骤日志以支持可解释性。

该项目基于 kube-batch 构建，属于 CNCF Sandbox 项目。