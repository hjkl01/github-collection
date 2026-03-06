
---
title: firecracker
---

### [firecracker-microvm firecracker](https://github.com/firecracker-microvm/firecracker)  ![GitHub Repo stars](https://img.shields.io/github/stars/firecracker-microvm/firecracker?style=social)

Firecracker 是一款开源虚拟化技术，旨在为容器和函数工作负载提供安全、多租户且低开销的执行环境。它基于 Linux KVM 创建轻量级微虚拟机（microVMs），结合硬件虚拟化的安全隔离性与容器的启动速度。Firecracker 采用极简设计以减少内存占用和攻击面，通过 API 提供 vCPU、内存、网络、磁盘及安全策略的动态配置能力。该项目主要用于加速无服务器操作模型，已在 AWS Lambda 和 Fargate 等生产服务中应用，并集成于 Kata Containers 等容器运行时。