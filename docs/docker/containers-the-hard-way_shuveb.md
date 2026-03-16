### [shuveb containers-the-hard-way](https://github.com/shuveb/containers-the-hard-way)  ![GitHub Repo stars](https://img.shields.io/github/stars/shuveb/containers-the-hard-way?style=social)

Gocker 是一个使用 Go 语言从零实现的迷你 Docker 容器引擎，旨在演示 Linux 系统调用层面的容器原理。其核心功能包括：

1. 镜像管理：从 Docker Hub 拉取、列出和删除本地镜像。
2. 容器操作：创建并运行容器、列出运行中的容器、在容器内执行进程。
3. 环境隔离：通过文件系统、PID、IPC、UTS、挂载和网络命名空间实现隔离。
4. 资源控制：基于 cgroups 限制 CPU、内存和进程数量。
5. 网络支持：利用 Overlay 文件系统并配置主机网络使容器可访问互联网。

该项目为纯 Go 源码实现，需以 root 权限在 Linux 环境下运行。