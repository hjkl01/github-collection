
---
title: skopeo
---

### [containers skopeo](https://github.com/containers/skopeo)  ![GitHub Repo stars](https://img.shields.io/github/stars/containers/skopeo?style=social)

Skopeo 是一个无需 root 权限和守护进程的命令行工具，用于操作容器镜像及仓库。它支持 OCI 和 Docker v2 镜像格式，可连接各类注册表、本地目录及 OCI 布局目录。主要功能包括：在不同存储机制间复制镜像、远程检查镜像属性（无需拉取至本地）、从仓库删除镜像以及同步镜像仓库（适用于离线部署）。此外，它还支持私有仓库的身份验证（登录/登出/凭据传递）、签名生成与验证，并提供 copy、inspect、sync、delete 等核心操作命令。