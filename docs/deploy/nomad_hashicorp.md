### [hashicorp nomad](https://github.com/hashicorp/nomad)  ![GitHub Repo stars](https://img.shields.io/github/stars/hashicorp/nomad?style=social)

Nomad 是一款简单且灵活的工作负载编排器，支持在本地及云环境中大规模部署和管理容器（Docker, Podman）、非容器化应用（Executable, Java）及虚拟机（QEMU）。

核心功能特性包括：

*   **混合编排**：支持容器与传统应用在相同基础设施上共存，无需强制容器化。
*   **简单可靠**：单二进制自包含系统，无需外部存储或协调服务，具备自动故障恢复和高可用性。
*   **硬件支持**：内置设备插件，自动识别并利用 GPU、FPGA、TPU 等硬件资源，适用于 AI/ML 工作负载。
*   **全球联邦**：支持跨多区域、跨云环境的部署与联邦，经实测可扩展至 10,000+ 节点集群。
*   **生态集成**：与 Terraform、Consul、Vault 无缝集成，提供资源供应、服务发现及密钥管理功能。
*   **跨平台**：全面兼容 Linux、Windows 和 macOS 操作系统。