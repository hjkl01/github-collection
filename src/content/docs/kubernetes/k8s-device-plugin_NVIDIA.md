
---
title: k8s-device-plugin
---

### [NVIDIA k8s-device-plugin](https://github.com/NVIDIA/k8s-device-plugin)  ![GitHub Repo stars](https://img.shields.io/github/stars/NVIDIA/k8s-device-plugin?style=social)

NVIDIA Kubernetes 设备插件是一个 Daemonset，核心功能是自动暴露节点 GPU 数量、监控 GPU 健康状态并支持运行 GPU 容器。它支持 CUDA 时间切片和 MPS 实现 GPU 资源共享，支持 Multi-Instance GPU (MIG) 策略及 IMEX 通道注入。支持通过 Helm 部署，集成 GPU Feature Discovery 实现自动节点打标，支持节点级配置。插件提供灵活的配置方式（命令行、环境变量、配置文件），兼容多种设备传递策略，并支持 CPU Manager。