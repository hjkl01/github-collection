
---
title: lima
---

### [lima-vm lima](https://github.com/lima-vm/lima)

**项目核心内容总结：**

**功能**  
Lima 是一个可在多平台（包括 macOS、Linux、NetBSD 等）运行的工具，用于创建 Linux 虚拟机，支持自动文件共享和端口转发（类似 WSL2）。除容器相关用途外，也可用于非容器应用。支持多种容器引擎（如 Docker、Podman、Kubernetes）。

**使用方法**  
1. 通过 Homebrew 安装：`brew install lima`，然后启动虚拟机：`limactl start`。  
2. 运行 Linux 命令：`lima uname -a`。  
3. 运行容器：  
   - 使用 containerd：`lima nerdctl run --rm hello-world`。  
   - 使用 Docker：先启动模板 `limactl start template://docker`，设置 `DOCKER_HOST` 环境变量后运行容器。  
   - 使用 Kubernetes：启动 `k8s` 模板并配置 `KUBECONFIG` 后使用 `kubectl`。

**主要特性**  
- 自动文件共享与端口转发  
- 支持多种容器引擎（Docker、Podman、Kubernetes 等）  
- 兼容非 macOS 主机（如 Linux、NetBSD）  
- 提供多种社区工具集成（如 Rancher Desktop、Colima、Podman Desktop 等）  
- 遵循 CNCF 规范，为孵化项目