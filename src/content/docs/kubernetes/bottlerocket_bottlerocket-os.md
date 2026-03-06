
---
title: bottlerocket
---

### [bottlerocket-os bottlerocket](https://github.com/bottlerocket-os/bottlerocket)  ![GitHub Repo stars](https://img.shields.io/github/stars/bottlerocket-os/bottlerocket?style=social)

Bottlerocket 是一款专为托管容器设计的免费开源 Linux 操作系统，致力于提供安全、可靠且易于维护的平台。

核心特性：
1. **安全性**：默认无 SSH 和 Shell，使用 dm-verity 实现不可变根文件系统，采用 SELinux 和 Rust 组件增强安全。
2. **配置管理**：通过 API 进行系统配置，设置随更新自动迁移，无需手动修改。
3. **更新机制**：基于分区翻转技术，支持快速系统更新、自动回滚及 TUF 安全校验。
4. **访问方式**：通过 Control 容器（集成 AWS SSM）或可选的 Admin 容器（支持 SSH）进行管理。
5. **适用场景**：主要支持 AWS EKS、Amazon ECS 和 VMware Kubernetes，兼容 NVIDIA 和 AWS Neuron 实例。
6. **系统架构**：包含根设备与数据设备（持久化存储），支持 x86_64 和 aarch64 架构，基于标准开源组件构建。