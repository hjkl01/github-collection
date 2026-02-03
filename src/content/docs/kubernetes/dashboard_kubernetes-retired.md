
---
title: dashboard
---

### [kubernetes-retired dashboard](https://github.com/kubernetes-retired/dashboard)  ![GitHub Repo stars](https://img.shields.io/github/stars/kubernetes-retired/dashboard?style=social)

**项目简介：**

Kubernetes Dashboard 是一个通用的、基于网页的 Kubernetes 集群管理界面。用户可以通过它管理在集群中运行的应用程序、排查问题，以及管理集群本身。

**核心功能：**

- 提供可视化的 Kubernetes 集群管理界面。
- 支持通过 Helm 安装（不再支持基于 Manifest 的安装方式）。
- 使用 Kong 网关 API 代理作为多容器架构的网关，简化部署。
- 模块化设计，每个模块独立版本管理。
- 提供用户指南、访问控制、开发指南等文档支持。

**使用方法：**

1. 添加 Helm 仓库：
   ```console
   helm repo add kubernetes-dashboard https://kubernetes.github.io/dashboard/
   ```

2. 安装 Dashboard：
   ```console
   helm upgrade --install kubernetes-dashboard kubernetes-dashboard/kubernetes-dashboard --create-namespace --namespace kubernetes-dashboard
   ```

**主要特性：**

- 支持 Helm 安装，简化部署流程。
- 提供详细的用户和开发者文档。
- 支持自定义安装配置（通过 Helm chart values）。
- 支持通过任意 Ingress 控制器或代理访问 Dashboard。
- 项目已归档，不再维护，建议使用替代方案 **Headlamp**。

**替代方案推荐：**

建议使用 **Headlamp**，一个由 Kubernetes 社区维护的现代 Kubernetes Web 界面。