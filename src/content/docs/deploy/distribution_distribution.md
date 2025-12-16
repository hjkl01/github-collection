
---
title: distribution
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/distribution/distribution?style=social) ](https://github.com/distribution/distribution)
### [distribution distribution](https://github.com/distribution/distribution)

该项目是用于存储、分发容器镜像及其他内容的开源注册表实现，基于[OCI Distribution Specification](https://github.com/opencontainers/distribution-spec)。其核心功能包括：  
- 提供简单、安全、可扩展的注册表基础，支持构建大规模系统或运行私有注册表；  
- 被 Docker Hub、GitHub Container Registry 等主流平台采用；  
- 包含 **registry**（OCI规范实现）、**libraries**（交互库，接口不稳定需注意）和 **documentation**（完整文档）三大组件。  

**使用方法**：通过 HTTP 协议与 OCI 兼容的客户端（如 Docker、containerd）通信。当前项目中的客户端已弃用，推荐使用 [containerd](https://github.com/containerd/containerd) 的实现。  

**主要特性**：  
- 遵循 OCI 标准，兼容主流容器工具；  
- 提供丰富的库和文档支持；  
- 长期目标是构建安全、专业的工具链，支持自定义扩展和多种部署场景。