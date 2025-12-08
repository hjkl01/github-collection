
---
title: containerd
---

### [containerd containerd](https://github.com/containerd/containerd)

containerd 是一个行业标准的容器运行时，专注于简单性、稳健性和可移植性，支持 Linux 和 Windows 系统，可管理容器的完整生命周期（包括镜像传输、存储、容器执行、网络配置等）。作为 CNCF 的毕业项目，其设计目标是嵌入到更大系统中，而非直接面向开发者或终端用户。  

**主要特性**：  
- 支持 OCI 标准的镜像仓库；  
- 提供 Kubernetes CRI 插件，兼容 Kubernetes 1.10 及以上版本；  
- 包含快照、检查点与恢复等功能；  
- 提供夜间构建版本（非生产环境推荐）；  
- 支持通过命令行工具 `ctr` 管理容器；  
- 采用 Apache 2.0 许可证，文档使用 Creative Commons 许可证。  

**使用方法**：  
- 通过 [containerd.io](https://containerd.io) 文档获取操作指南、命名空间配置及客户端选项说明；  
- 参考 `Getting Started.md` 入门；  
- 使用 `cri` 插件时，可通过 `crictl` 工具调试容器和镜像。  

**其他**：  
- 社区提供安全审计和漏洞报告渠道；  
- 支持通过 GitHub 参与贡献，包含新手友好议题；  
- 采用模块化架构，支持多种存储驱动（如 overlay、btrfs）。