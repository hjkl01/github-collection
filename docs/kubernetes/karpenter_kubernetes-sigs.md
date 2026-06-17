### [karpenter](https://github.com/kubernetes-sigs/karpenter) ![GitHub Repo stars](https://img.shields.io/github/stars/kubernetes-sigs/karpenter?style=social)

Karpenter是Kubernetes集群自动扩展工具，通过以下方式提高效率并降低成本：

- 监控调度器标记为不可调度的Pod
- 评估Pod的调度约束（资源请求、节点选择器、亲和性、容忍度、拓扑分布约束）
- 动态调配满足Pod需求的节点
- 自动移除不再需要的节点

支持多云部署，包括AWS、Azure、GCP、阿里云、IBM Cloud等云服务商。