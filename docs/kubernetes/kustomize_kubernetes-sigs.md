### [kubernetes-sigs kustomize](https://github.com/kubernetes-sigs/kustomize)  ![GitHub Repo stars](https://img.shields.io/github/stars/kubernetes-sigs/kustomize?style=social)

Kustomize 是用于定制 Kubernetes 原始、无模板 YAML 文件的工具，在保持原文件不变的前提下理解并补丁 Kubernetes API 对象。它通过 kustomization 文件声明资源及自定义配置，支持通过 overlays 管理多环境变体（如开发、生产），将基础配置与环境特定补丁组合生成最终 YAML。该工具可独立运行生成 YAML 应用于集群，也可与 kubectl 集成使用。