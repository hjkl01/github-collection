
---
title: podman
---

### [containers podman](https://github.com/containers/podman)  ![GitHub Repo stars](https://img.shields.io/github/stars/containers/podman?style=social)

Podman 是一款用于管理 OCI 容器、镜像、卷及 Pod 的开源工具。它支持在 Linux、Mac 和 Windows 系统上运行（非 Linux 平台通过虚拟机），采用无守护进程架构，有效提升安全性并降低资源占用。核心功能涵盖支持 OCI 和 Docker 镜像格式的完整生命周期管理（构建、拉取、运行、检查点恢复等），提供兼容 Docker 的 CLI 界面和 REST API，支持无 Root 权限运行（Rootless）、资源隔离及基于 Netavark 的网络管理。项目与 Buildah 互补，Buildah 专注于镜像构建，Podman 侧重于生产环境中的容器与镜像管理。