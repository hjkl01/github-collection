
---
title: lima
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/lima-vm/lima?style=social) ](https://github.com/lima-vm/lima)
### [lima-vm lima](https://github.com/lima-vm/lima)

**Lima 是一个用于启动 Linux 虚拟机的工具，支持自动文件共享和端口转发（类似 WSL2）。**  
- **功能**：可运行 Linux 命令、容器（基于 containerd、Docker、Kubernetes 等）及非容器应用；支持多种主机系统（包括 macOS、Linux、NetBSD 等）。  
- **使用方法**：通过 Homebrew 安装后，使用 `limactl start` 启动虚拟机；运行命令如 `lima uname -a`、`lima nerdctl run` 或配置 Docker/Kubernetes 环境。  
- **特性**：集成 containerd 和 nerdctl，支持多容器引擎；作为 CNCF 孵化项目，提供跨平台兼容性。