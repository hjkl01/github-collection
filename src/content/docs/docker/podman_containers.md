
---
title: podman
---

### [containers podman](https://github.com/containers/podman)

**Podman 核心内容总结：**

**项目功能**  
Podman 是一款用于管理容器、镜像、卷和容器组（Pod）的工具，支持 OCI 和 Docker 镜像格式。它提供完整的容器生命周期管理（创建、运行、停止、删除），支持通过容器文件（Containerfile/Dockerfile）构建镜像，并可推送到镜像仓库。Podman 无需依赖守护进程，提升安全性与资源利用率。

**主要特性**  
1. **无守护进程架构**：无需后台服务，直接运行容器，降低资源占用。  
2. **Rootless 模式**：支持以普通用户身份运行容器，通过用户命名空间隔离权限，增强安全性。  
3. **跨平台支持**：在 Linux 上原生运行，通过虚拟机支持 Mac 和 Windows。  
4. **网络管理**：集成 Netavark 实现容器网络配置，支持 rootless 网络（如 slirp4netns）。  
5. **Pod 支持**：管理共享资源的容器组，实现多容器协同。  
6. **兼容 Docker CLI**：提供与 Docker 兼容的命令行接口，支持远程操作。  
7. **REST API**：提供 Docker 兼容及高级功能接口，便于集成。  

**使用方法**  
- 安装后通过命令行运行容器（如 `podman run quay.io/podman/hello`）。  
- 支持镜像拉取、构建（通过 Buildah）、容器管理（启动、停止、删除）。  
- 在非 Linux 系统使用 `podman machine` 虚拟机运行容器。  
- 通过 Podman Desktop 图形化界面管理容器和 Kubernetes。  

**技术协作**  
- 与 Buildah 协作：Buildah 负责镜像构建，Podman 负责镜像管理与容器运行。  
- 依赖 OCI 项目：使用 containers/image（镜像管理）、containers/storage（存储）、Netavark（网络）等开源库。  

**适用场景**  
适合需要安全、高效容器管理的开发环境，支持生产环境与本地开发，兼容 Docker 工作流。
