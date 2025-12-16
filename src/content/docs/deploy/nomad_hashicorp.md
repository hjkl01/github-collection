
---
title: nomad
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/hashicorp/nomad?style=social) ](https://github.com/hashicorp/nomad)
### [hashicorp nomad](https://github.com/hashicorp/nomad)

**项目核心内容总结：**  
Nomad 是 HashiCorp 开发的轻量级工作负载编排工具，支持容器（Docker、Podman）、非容器化应用（如 Java、可执行文件）和虚拟机（QEMU）的统一部署与管理，适用于本地和云环境。支持 Linux、Windows、macOS，企业版提供额外功能。  

**主要特性：**  
1. **灵活部署**：兼容容器、传统应用和批量任务，无需容器化即可利用任务驱动器。  
2. **高可靠性**：单二进制文件运行，内置资源管理与调度，自动处理故障，支持高可用性。  
3. **硬件支持**：通过设备插件支持 GPU、FPGA、TPU 等硬件资源。  
4. **多云扩展**：原生支持跨多区域、多云部署。  
5. **可扩展性**：乐观并发设计，支持 10,000+ 节点集群。  
6. **生态集成**：与 Terraform、Consul、Vault 等 HashiCorp 工具无缝协作。  

**使用方法：**  
- **测试环境**：通过官方教程快速搭建本地集群，或使用 Terraform 模板在云上部署开发集群。  
- **生产环境**：参考官方推荐的生产架构文档进行部署。  
- **文档与支持**：提供完整文档、API 参考、教程及社区论坛。