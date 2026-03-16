### [GoogleContainerTools distroless](https://github.com/GoogleContainerTools/distroless)  ![GitHub Repo stars](https://img.shields.io/github/stars/GoogleContainerTools/distroless?style=social)

Distroless 项目提供精简容器镜像，仅包含应用程序及其运行时依赖，不包含包管理器、Shell 或标准 Linux 发行版工具。其核心功能与特点如下：

1. **体积与安全**：镜像体积极小（最小约 2 MiB），显著降低攻击面，优化 CVE 扫描信噪比。
2. **基础环境**：基于 Debian 12 和 13 构建，支持多种 CPU 架构。
3. **语言支持**：提供静态镜像及 Java、Node.js、Python3 等多种语言运行时环境。
4. **构建集成**：支持通过 Docker 多阶段构建或 Bazel 工具生成镜像。
5. **维护调试**：镜像经 cosign 签名验证，提供 Debug 版本用于调试，并自动同步 Debian 安全更新。