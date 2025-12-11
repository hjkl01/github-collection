
---
title: firecracker
---

### [firecracker-microvm firecracker](https://github.com/firecracker-microvm/firecracker)

**项目核心内容总结：**

**功能**  
Firecracker 是一个开源的虚拟化技术，用于创建和管理轻量级微虚拟机（microVM），提供安全、多租户的容器和函数工作负载执行环境，适用于无服务器架构（如 AWS Lambda 和 Fargate）。

**使用方法**  
- 通过下载发布版本或从源码构建（需 Unix/Linux 系统、Docker 和 bash）。  
- 构建命令示例：`git clone` 后执行 `tools/devtool build`，生成的二进制文件位于 `build/cargo_target/.../debug/firecracker`。  
- 详细步骤见 [快速入门指南](docs/getting-started.md)。

**主要特性**  
1. **轻量安全**：通过移除冗余设备和功能，减少内存占用和攻击面，提升启动速度与安全性。  
2. **灵活配置**：支持自定义 vCPU、内存、网络接口、磁盘、vsock、熵设备、持久内存设备等。  
3. **API 控制**：提供 OpenAPI 格式的接口，可动态管理微虚拟机（如启动、停止、配置资源限制）。  
4. **高级功能**：内置需求分页、CPU 超分、线程级 seccomp 过滤、Jailer 进程隔离等。  
5. **兼容性**：支持多种主机操作系统（如 Amazon Linux、Ubuntu）和内核版本，覆盖 Intel/AMD/Graviton 多种芯片架构。  

**开源协议**：Apache 2.0，适用于生产环境。