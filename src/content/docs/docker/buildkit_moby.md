
---
title: buildkit
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/moby/buildkit?style=social) ](https://github.com/moby/buildkit)
### [moby buildkit](https://github.com/moby/buildkit)

**BuildKit 核心内容总结：**

**项目功能：**  
BuildKit 是一个用于构建容器镜像的工具，支持多种构建方式（如 Dockerfile）、多平台镜像构建、构建元数据输出（如镜像摘要），并兼容多种容器运行环境（Docker、Podman、Nerdctl、Kubernetes）。

**使用方法：**  
- 通过 `buildctl` 命令行工具操作，支持与本地或远程 BuildKit 守护进程通信。  
- 可运行于系统级（Systemd socket 激活、TCP 服务）、容器化环境（Docker/Podman/Nerdctl 容器）或 Kubernetes 部署。  
- 支持“无守护进程模式”（daemonless），在单个容器中同时运行客户端和临时守护进程。

**主要特性：**  
- **多平台构建**：支持跨架构镜像构建（如 x86 到 ARM）。  
- **可扩展性**：支持 OpenTelemetry 追踪（集成 Jaeger 等工具）。  
- **灵活性**：可自定义日志输出颜色、调整 TTY 模式下的日志行数。  
- **安全性**：支持无 root 权限运行（rootless 模式）。  
- **容器化部署**：提供官方镜像（如 `moby/buildkit`），支持多种运行环境。