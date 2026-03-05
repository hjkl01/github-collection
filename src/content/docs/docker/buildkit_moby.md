
---
title: buildkit
---

### [moby buildkit](https://github.com/moby/buildkit)  ![GitHub Repo stars](https://img.shields.io/github/stars/moby/buildkit?style=social)

BuildKit 是一个高效、可扩展的工具包，用于将源代码转换为构建产物。其核心组件为 `buildkitd` 守护进程和 `buildctl` 客户端。

主要功能特性：
1. **高效构建**：支持指令缓存、自动垃圾回收、并发依赖解析及无 Root 权限运行。
2. **可扩展前端**：基于 LLB 中间格式，支持 Dockerfile、Buildpacks、HLB 等多种构建定义。
3. **多样输出**：支持将结果输出为镜像仓库、本地目录、Docker/OCI tarball 或 containerd 存储。
4. **灵活缓存**：支持本地、Registry、S3、Azure Blob Storage 及 GitHub Actions 等多种缓存后端。
5. **架构灵活**：支持分布式 Workers、TCP 服务暴露、Systemd socket 激活及容器化部署。

该工具被 Docker、Kubernetes、Tekton 及多种 CI/CD 平台广泛采用。