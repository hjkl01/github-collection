
---
title: kustomize
---

### [kubernetes-sigs kustomize](https://github.com/kubernetes-sigs/kustomize)  ![GitHub Repo stars](https://img.shields.io/github/stars/kubernetes-sigs/kustomize?style=social)

kustomize 是一个面向 Kubernetes 的 YAML 自定义工具，无需模板即可对原始 YAML 文件进行定制。它通过 `kustomization.yaml` 声明式配置资源及定制内容（如添加标签、生成 ConfigMap），通过打补丁方式生成定制 YAML 而保留原文件不变。支持基础配置与覆盖配置（overlays）的分层管理，便于针对不同环境（如开发、生产）管理配置变体。支持独立运行或由 kubectl 内置调用，直接构建配置并应用至集群。