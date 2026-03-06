
---
title: k8s-device-plugin
---

### [NVIDIA k8s-device-plugin](https://github.com/NVIDIA/k8s-device-plugin)  ![GitHub Repo stars](https://img.shields.io/github/stars/NVIDIA/k8s-device-plugin?style=social)

NVIDIA Kubernetes Device Plugin 实现了 Kubernetes 官方 Device Plugin API，部署为 Daemonset 用于自动管理集群中的 NVIDIA GPU 资源。其主要功能包括暴露节点 GPU 数量与健康状态、支持容器通过 `nvidia.com/gpu` 资源调度 GPU。项目支持 CUDA 时间切片和 MPS 技术以实现 GPU 资源共享与超分，并提供 Multi-Instance GPU (MIG)、IMEX 通道注入、GPU 特征发现自动标签及 CPUManager 兼容性等高级特性。用户可通过命令行、环境变量、配置文件或 Helm Chart 进行灵活配置与部署。