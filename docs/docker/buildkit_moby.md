### [moby buildkit](https://github.com/moby/buildkit)  ![GitHub Repo stars](https://img.shields.io/github/stars/moby/buildkit?style=social)

BuildKit 是一款将源代码高效、可重复地转换为构建产物的工具集。

核心功能：
1. **构建支持**：兼容 Dockerfile、Buildpacks、LLB 等多种前端格式，支持多平台构建。
2. **组件架构**：由 `buildkitd` 守护进程和 `buildctl` 客户端组成，支持 Linux、macOS 及 Windows 平台。
3. **缓存管理**：提供自动垃圾回收，支持缓存导入/导出至镜像仓库、本地、S3、Azure 及 GitHub Actions 等多种存储。
4. **输出格式**：支持输出为容器镜像、本地目录、Docker 或 OCI Tarball 包及 containerd 存储。
5. **扩展性与部署**：采用插件化架构，支持分布式 Worker、无根权限运行、TLS 加密 TCP 服务，支持容器化部署（Docker、Kubernetes）及无守护进程模式。
6. **可观测性**：集成 OpenTelemetry 支持构建追踪，支持元数据输出。