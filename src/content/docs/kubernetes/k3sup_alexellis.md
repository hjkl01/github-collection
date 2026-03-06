
---
title: k3sup
---

### [alexellis k3sup](https://github.com/alexellis/k3sup)  ![GitHub Repo stars](https://img.shields.io/github/stars/alexellis/k3sup?style=social)

k3sup 是一个轻量级工具，用于通过 SSH 在本地或远程虚拟机（包括云服务器、树莓派、物理机）上快速安装 k3s（轻量级 Kubernetes），并自动获取 KUBECONFIG 文件，使用户能立即使用 kubectl 管理集群。

主要功能如下：

1. **快速部署与连接**：通过 `install` 命令远程安装 k3s 服务器节点，并自动将 kubeconfig 同步到本地；通过 `join` 命令将代理节点加入集群。
2. **高可用集群**：支持配置多主（HA）集群，可选择嵌入式 etcd 或外部 SQL 数据库作为数据存储。
3. **社区版 (CE)**：基础安装、本地模式支持、配置合并及自定义参数。
4. **专业版 (Pro)**：
   - 支持 `plan` 和 `apply` 命令，基于文件进行大规模集群的自动化、并行安装及 GitOps 管理。
   - 支持 `uninstall` 并行卸载集群。
   - 支持 `exec` 在集群所有节点执行命令。
   - 支持从现有集群拉取 kubeconfig (`get-config`)。

该工具旨在简化 Kubernetes 的引导过程，实现从零到 kubectl 可用状态在 60 秒内完成。