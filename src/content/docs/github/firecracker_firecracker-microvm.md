
---
title: firecracker
---

### [firecracker-microvm firecracker](https://github.com/firecracker-microvm/firecracker)  ![GitHub Repo stars](https://img.shields.io/github/stars/firecracker-microvm/firecracker?style=social)

Firecracker 是一款开源虚拟化技术，旨在安全、多租户地低开销执行容器和函数工作负载。它基于 Linux KVM 创建轻量级虚拟机（microVMs），结合硬件虚拟化的安全隔离性与容器的速度灵活性。项目核心采用极简 VMM 设计，通过剔除不必要设备降低内存占用和攻击面，从而提升安全性、启动速度和硬件利用率。Firecracker 提供 API 接口管理微虚拟机资源（vCPU、内存、网络、磁盘等），并内置 seccomp 安全过滤器与 Jailer 进程以增强隔离。该项目由 AWS 开发，用于加速 Lambda 和 Fargate 等服务，已开源并集成于 Kata Containers 等运行时。