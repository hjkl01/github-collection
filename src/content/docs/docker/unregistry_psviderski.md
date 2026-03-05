
---
title: unregistry
---

### [psviderski unregistry](https://github.com/psviderski/unregistry)  ![GitHub Repo stars](https://img.shields.io/github/stars/psviderski/unregistry?style=social)

Unregistry 是一个轻量级容器镜像注册表，允许通过 `docker pussh` 命令将 Docker 镜像直接推送到远程服务器，无需外部注册中心。

**核心功能：**
1. **直达传输**：通过 SSH 隧道传输镜像缺失层，效率类似 `rsync`。
2. **免配置**：无需注册表服务、订阅或暴露端口，无中间存储。
3. **存储优化**：基于 containerd 存储，避免镜像冗余。
4. **多场景适用**：支持生产部署、CI/CD 及隔离网络环境。

**前提条件：** 本地与远程服务器需安装 Docker 和 OpenSSH，且远程用户具备 Docker 执行权限。