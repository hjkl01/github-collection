### [meshery meshery](https://github.com/meshery/meshery)  ![GitHub Repo stars](https://img.shields.io/github/stars/meshery/meshery?style=social)

Meshery 是云原生计算基金会（CNCF）旗下的开源云原生管理器，作为自助式工程平台，用于设计和管理工作所有基于 Kubernetes 的多云基础设施及应用。

核心功能包括：
1. **基础设施生命周期管理**：支持 300 多种云原生集成，管理云服务和 K8s 集群的配置、部署及运维。
2. **多集群多云管控**：提供统一视图管理跨云 K8s 集群，确保配置、操作及可观测性的一致性。
3. **可视化 GitOps**：基于 GitOps 方法，可视化协作设计基础设施，智能推断资源关系。
4. **部署模拟验证**：支持干运行（Dry-run）模拟部署，验证配置合法性并预览变更，防止生产环境错误。
5. **策略合规管理**：集成 Open Policy Agent，强制执行配置最佳实践，无需编写 Rego 查询。
6. **工作区与协作**：通过工作空间组织项目，管理环境连接，支持在 Pull Request 中预览基础设施变更。
7. **平台扩展性**：支持插件、API 等多种扩展点，可作为内部开发者平台基础，提供多租户隔离与 RBAC。
8. **性能分析**：提供负载生成、性能特征分析及历史性能跟踪，基于 SMP 标准比较性能指标。