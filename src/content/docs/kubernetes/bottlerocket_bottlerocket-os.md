
---
title: bottlerocket
---

### [bottlerocket-os bottlerocket](https://github.com/bottlerocket-os/bottlerocket)  ![GitHub Repo stars](https://img.shields.io/github/stars/bottlerocket-os/bottlerocket?style=social)

Bottlerocket OS 是一款专为托管容器设计的自由开源 Linux 操作系统，聚焦于安全性和可维护性，为容器工作负载提供可靠、一致且安全的平台。

主要功能特性包括：
1. **API 驱动配置**：通过 API 管理系统设置，支持配置在更新时自动迁移，避免手动维护。
2. **安全更新机制**：采用分区翻转和 TUF 技术进行系统更新，支持快速更新及失败自动回滚。
3. **高安全性设计**：默认禁用 SSH 和 Shell，集成 dm-verity、SELinux，核心组件多用 Rust 编写。
4. **多环境支持**：提供 AWS EKS、ECS、VMware Kubernetes 及裸金属等多种变体，支持 x86_64 和 aarch64 架构。
5. **灵活访问方式**：默认通过 Control 容器（基于 AWS SSM）访问，可启用 Admin 容器以获取 SSH 访问权限。

该系统适用于运行在 Amazon EKS、ECS、VMware 或裸金属服务器上的容器化工作负载。