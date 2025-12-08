
---
title: kata-containers
---

### [kata-containers kata-containers](https://github.com/kata-containers/kata-containers)

**Kata Containers 核心内容总结：**

1. **项目功能**  
   Kata Containers 是一个开源项目，提供轻量级虚拟机（VM）实现，兼具容器的性能与虚拟机的隔离安全性，适用于需要高安全性和隔离性的容器化场景。

2. **使用方法**  
   - 通过 `kata-runtime check` 命令检查系统是否支持运行 Kata Containers。  
   - 安装方法参考官方文档 [安装指南](docs/install)。  
   - 配置通过单个配置文件实现，支持运行时、代理和 hypervisor 等组件的配置。

3. **主要特性**  
   - **多平台支持**：兼容 x86_64、ARM（aarch64）、Power（ppc64le）和 IBM Z（s390x）架构，支持 Intel VT-x、AMD SVM、ARM Hyp 等虚拟化技术。  
   - **核心组件**：包含运行时（runtime）、代理（agent）、hypervisor 以及可选的内置 VMM（dragonball）。  
   - **开发与测试**：提供开发者指南、测试工具（如 kata-ctl、agent-ctl）及 CI 流水线配置。  
   - **文档与社区**：包含架构设计、安装配置、安全规范等文档，社区贡献可通过 [community 仓库](https://github.com/kata-containers/community) 参与。

4. **许可证**  
   采用 Apache 2.0 协议开源。  

5. **其他**  
   - 提供调试工具（如 kata-debug）和 Kubernetes 集群调试支持。  
   - 支持通过 OCI 标准运行容器（如 runk 工具）。