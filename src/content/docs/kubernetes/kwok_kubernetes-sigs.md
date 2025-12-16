
---
title: kwok
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/kubernetes-sigs/kwok?style=social) ](https://github.com/kubernetes-sigs/kwok)
### [kubernetes-sigs kwok](https://github.com/kubernetes-sigs/kwok)

**项目核心内容总结：**  
KWOK 是一个用于模拟 Kubernetes 集群节点和资源的工具，可快速创建数千个节点和 Pod，资源占用极低。  

**功能与使用方法：**  
- 提供 `kwok`（模拟节点、Pod 等资源生命周期）和 `kwokctl`（集群创建与管理）两个工具。  
- 支持通过预构建镜像（需 Docker 或 Nerdctl）或二进制文件安装，兼容 Kubernetes API 工具（如 kubectl、Helm）。  

**主要特性：**  
1. **轻量高效**：可在笔记本电脑上模拟 1000 个节点和 10 万个 Pod，资源消耗低。  
2. **快速部署**：秒级创建/删除集群和节点，支持每秒生成 20 个节点或 Pod。  
3. **高度兼容**：适配所有 Kubernetes API 客户端，无需额外适配。  
4. **跨平台灵活**：无硬件依赖，支持自定义节点标签、污点、容量等参数，可模拟复杂场景。