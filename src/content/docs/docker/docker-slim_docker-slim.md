
---
title: docker-slim
---

### [docker-slim docker-slim](https://github.com/docker-slim/docker-slim)  ![GitHub Repo stars](https://img.shields.io/github/stars/docker-slim/docker-slim?style=social)

Slim（原名 DockerSlim）是一个 CNCF Sandbox 项目，旨在优化容器体验，使容器镜像更小、更安全且易用。

**核心功能：**

1.  **镜像精简**：通过静态和动态分析自动移除容器中的冗余组件，无需修改 Dockerfile 或工作流，即可将镜像大小大幅缩小（最高可达数十倍）。
2.  **安全加固**：基于应用运行时行为自动生成 Seccomp 和 AppArmor 安全配置文件，减少攻击面并提升安全性。
3.  **多语言与基础镜像支持**：兼容 Node.js、Python、Java、Go、Rust 等多种语言栈，支持 Ubuntu、Alpine、Distroless 等多种基础镜像。
4.  **分析与管理工具**：提供 `build`（构建优化镜像）、`xray`（静态分析）、`lint`（检查）、`debug`（调试）、`registry`（注册表操作）等 CLI 命令。
5.  **生态集成**：支持容器化运行，并可无缝集成至 Jenkins、GitHub Actions 等 CI/CD 流程中。