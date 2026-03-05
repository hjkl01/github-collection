
---
title: skopeo
---

### [containers skopeo](https://github.com/containers/skopeo)  ![GitHub Repo stars](https://img.shields.io/github/stars/containers/skopeo?style=social)

Skopeo 是一个无需 root 权限或守护进程即可运行的命令行工具，用于管理容器镜像和仓库。它支持 OCI 和 Docker v2 镜像标准，可对接各类容器镜像注册表、本地目录及 OCI 布局目录。主要功能包括跨存储机制复制镜像、检查远程镜像属性（无需拉取至本地）、删除镜像、同步仓库（适用于离线部署）以及管理认证凭证。支持多种存储后端（如 containers-storage、dir、docker-daemon、oci 等），并提供 copy、inspect、delete、sync、login 等核心命令。