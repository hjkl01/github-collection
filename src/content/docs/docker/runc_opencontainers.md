
---
title: runc
---

### [opencontainers runc](https://github.com/opencontainers/runc)  ![GitHub Repo stars](https://img.shields.io/github/stars/opencontainers/runc?style=social)

runc 是一个遵循 OCI 规范的 Linux 命令行工具，用于启动和运行容器。作为底层容器运行时，它主要供 Docker 等高级容器软件调用，一般不直接面向终端用户。其核心功能包括管理容器生命周期（创建、启动、停止、删除）、支持无根容器模式、检查点与恢复功能，以及通过构建标签定制安全特性（如 Seccomp）。项目仅支持 Linux 平台构建与运行。