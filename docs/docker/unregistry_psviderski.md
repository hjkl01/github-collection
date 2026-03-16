### [psviderski unregistry](https://github.com/psviderski/unregistry)  ![GitHub Repo stars](https://img.shields.io/github/stars/psviderski/unregistry?style=social)

Unregistry 是一个轻量级容器镜像工具，允许用户通过 `docker pussh` 命令将 Docker 镜像直接推送到远程服务器，无需依赖外部注册表服务。

核心功能：
- **无中间存储**：通过 SSH 隧道在远程服务器启动临时容器传输镜像，传输后自动清理，无需维护自建注册服务。
- **增量传输**：仅传输缺失的镜像层，效率类似于 Docker 的 `rsync`，节省带宽。
- **安全便捷**：不暴露端口，无需配置外部存储或订阅第三方服务。
- **多场景适用**：适用于生产部署、CI/CD 流水线以及离线或隔离环境。

前提条件：本地及远程服务器需安装 Docker 和 OpenSSH，远程用户需具备 Docker 操作权限。