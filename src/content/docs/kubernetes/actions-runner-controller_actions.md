
---
title: actions-runner-controller
---

### [actions actions-runner-controller](https://github.com/actions/actions-runner-controller)  ![GitHub Repo stars](https://img.shields.io/github/stars/actions/actions-runner-controller?style=social)

Actions Runner Controller (ARC) 是一个 Kubernetes 运算符，用于编排和扩展 GitHub Actions 的自建运行器。它支持创建自动伸缩的运行器规模集（Runner Scale Sets），能够根据仓库、组织或企业的工作流数量自动扩展或缩减基于容器的临时运行器实例。项目可通过 Helm 部署至 Kubernetes 环境，实现运行器的弹性伸缩管理。