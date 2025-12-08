
---
title: containers-the-hard-way
---

### [shuveb containers-the-hard-way](https://github.com/shuveb/containers-the-hard-way)

**项目核心内容总结：**

**功能**  
Gocker 是一个用 Go 编写的轻量级 Docker 实现，用于演示容器如何通过 Linux 系统调用（如命名空间和 cgroups）工作。支持以下操作：  
- 创建并运行容器（如 `gocker run ubuntu /bin/bash`）；  
- 列出运行中的容器（`gocker ps`）；  
- 在运行中的容器内执行新命令（`gocker exec [容器ID] /bin/bash`）；  
- 管理镜像（下载、挂载）；  
- 通过 Overlay 文件系统实现镜像分层。  

**使用方法**  
1. 克隆项目后，使用 `go mod download` 安装依赖，再通过 `go build -o gocker .` 构建可执行文件。  
2. 首次运行需通过脚本 `enable_internet.sh` 配置网络，使容器可访问互联网。  
3. 命令行操作示例：  
   - `gocker run [镜像名] [命令]`：启动容器；  
   - `gocker ps`：查看运行中的容器；  
   - `gocker exec [容器ID] [命令]`：在容器内执行命令。  

**主要特性**  
- **资源隔离**：基于 Linux 命名空间（如网络、进程）实现容器隔离；  
- **资源限制**：支持通过 cgroups 限制 CPU、内存和进程数；  
- **网络功能**：自动创建 `gocker0` 桥接网络，容器间可通信；  
- **镜像管理**：依赖 GoContainerRegistry 从 Docker Hub 下载镜像；  
- **轻量设计**：无复杂代理功能（如端口映射），适合学习容器底层原理。  

**注意事项**  
- 需以 root 权限运行，可能对系统造成影响（如创建桥接网络、挂载文件系统）；  
- 当前不支持端口暴露、错误处理不完善。