
---
title: distroless
---

### [GoogleContainerTools distroless](https://github.com/GoogleContainerTools/distroless)  ![GitHub Repo stars](https://img.shields.io/github/stars/GoogleContainerTools/distroless?style=social)

"Distroless" 容器镜像项目提供仅包含应用程序及其运行时依赖的极简镜像，不含包管理器、Shell 或其他标准 Linux 程序。其优势在于镜像体积极小（最小约 2 MiB），能显著减少攻击面并提升安全扫描准确性。镜像基于 Debian 12/13 构建，支持多架构，提供静态、C/C++、Java、Python、Node.js 等多种运行时版本。用户可通过 Docker 多阶段构建或 Bazel 使用该镜像。所有镜像均经 cosign 签名以确保安全，并提供含 busybox 的调试镜像版本。该项目已被 Kubernetes 等广泛采用。