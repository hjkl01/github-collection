
---
title: bottlerocket
---

### [bottlerocket-os bottlerocket](https://github.com/bottlerocket-os/bottlerocket)

**Bottlerocket 项目核心内容总结**  

**项目功能**  
Bottlerocket 是一个轻量级、安全的操作系统，专为容器化应用和云环境优化，支持 Kubernetes 和 Amazon ECS。提供自动更新、安全启动、容器运行时（如 containerd）及与云服务（如 AWS）的深度集成。  

**使用方法**  
1. **配置方式**：通过 API 或容器编排工具（如 `kubectl`）管理；启动时可通过用户数据（TOML 格式）自动初始化配置。  
2. **部署支持**：兼容 AWS EC2、Kubernetes 和 ECS，支持 NVIDIA GPU 及 AWS Neuron 加速实例。  
3. **更新机制**：采用双分区（A/B）更新，失败时自动回滚；依赖 TUF 安全协议保障镜像完整性。  

**主要特性**  
- **安全防护**：  
  - 使用 dm-verity 验证不可变根文件系统，结合 SELinux 防止未授权访问。  
  - 多数组件用 Rust 编写，减少内存安全漏洞。  
- **高效更新**：分区切换实现无缝升级，记录成功启动记录以保障可靠性。  
- **包管理**：基于 RPM 定义构建，集成 Linux 内核、systemd、containerd 等核心组件。  
- **存储结构**：  
  - 根设备：存放系统分区、启动加载器及 API 数据存储。  
  - 数据设备（`/local`）：用于持久化容器镜像、主机容器及启动容器数据。  
- **硬件兼容性**：支持 NVIDIA GPU（驱动版本需匹配实例类型）及 AWS Neuron 加速实例（如 inf1、trn1）。  

**适用场景**  
适用于需要高安全性和自动化的云原生应用部署，尤其适合 AWS 生态中的容器化工作负载。