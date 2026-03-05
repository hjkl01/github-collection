
---
title: k3sup
---

### [alexellis k3sup](https://github.com/alexellis/k3sup)  ![GitHub Repo stars](https://img.shields.io/github/stars/alexellis/k3sup?style=social)

k3sup 是一款轻量级命令行工具，通过 SSH 在远程或本地 VM 上快速安装 k3s 并自动获取 KUBECONFIG，实现本地即刻使用 kubectl 管理集群。支持 Linux、Windows、macOS 及树莓派等平台。

核心功能：
*   **社区版 (CE)**：一键安装 k3s 服务器、加入代理节点、合并配置，支持多主高可用（HA）部署。
*   **专业版 (Pro)**：提供 IaC/GitOps 体验，支持通过计划文件自动化并行大规模部署、批量执行命令、获取现有集群配置及快速卸载。

该工具旨在简化 Kubernetes 初始化流程，仅需 SSH 访问和工具二进制文件即可完成集群搭建。