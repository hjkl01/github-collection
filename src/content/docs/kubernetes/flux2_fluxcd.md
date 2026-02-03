
---
title: flux2
---

### [fluxcd flux2](https://github.com/fluxcd/flux2)  ![GitHub Repo stars](https://img.shields.io/github/stars/fluxcd/flux2?style=social)

**项目功能**：Flux v2 是一个 Kubernetes 工具，用于将集群配置与 Git 仓库、OCI 镜像等源保持同步，并通过自动化更新配置实现持续交付。  

**使用方法**：通过提供的快速入门指南部署 Flux，支持 GitOps 方式管理应用。详细文档涵盖仓库结构、Helm 发布、镜像更新及密钥管理等场景。  

**主要特性**：  
- 基于 Kubernetes API 扩展系统，集成 Prometheus 等核心组件；  
- 支持多租户、多 Git 仓库同步；  
- 提供 GitOps Toolkit（包含 Source Controller、Kustomize Controller、Helm Controller 等组件），支持自定义资源（CRD）扩展；  
- 通过 Image Automation 实现镜像自动更新；  
- 与 CNCF 生态集成，被多家云厂商和企业采用。  

**核心组件**：包括 Git/OCI/Helm 资源同步、Kustomize/Helm 发布管理、通知系统（Alert/Receiver）及镜像策略自动化（ImagePolicy/UpdateAutomation）。