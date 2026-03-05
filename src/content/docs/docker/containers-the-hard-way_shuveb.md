
---
title: containers-the-hard-way
---

### [shuveb containers-the-hard-way](https://github.com/shuveb/containers-the-hard-way)  ![GitHub Repo stars](https://img.shields.io/github/stars/shuveb/containers-the-hard-way?style=social)

Gocker 是用 Go 语言从零实现的核心 Docker 功能工具，旨在展示 Linux 容器在系统调用层面的工作原理。

主要功能：
1. **镜像管理**：支持从 Docker Hub 拉取、查看及删除容器镜像。
2. **容器运行**：支持创建容器、列出运行中容器、在现有容器中执行命令。
3. **资源控制**：通过 Cgroups 限制容器使用的 CPU、内存和进程数。
4. **环境隔离**：利用 Linux 命名空间（文件系统、PID、IPC、UTS、Mount、Network）和 Overlay 文件系统实现隔离。
5. **网络支持**：容器拥有独立网络命名空间，经配置后可访问互联网。

注意：运行需 root 权限，目前不支持端口暴露。