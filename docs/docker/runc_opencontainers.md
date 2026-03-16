### [opencontainers runc](https://github.com/opencontainers/runc)  ![GitHub Repo stars](https://img.shields.io/github/stars/opencontainers/runc?style=social)

runc 是一款基于 OCI 规范的 Linux 命令行工具，用于创建和运行容器。它主要作为底层运行时供 Docker 等上层软件调用，而非直接面向终端用户。支持 OCI Bundle 管理、容器生命周期控制、无根（Rootless）模式运行、seccomp 过滤及检查点与恢复等功能。仅支持 Linux 平台。