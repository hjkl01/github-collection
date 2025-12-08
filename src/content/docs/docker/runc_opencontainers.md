
---
title: runc
---

### [opencontainers runc](https://github.com/opencontainers/runc)

**项目核心内容总结：**  
`runc` 是一个基于 OCI 规范的 CLI 工具，用于在 Linux 上创建和运行容器。  

**功能与使用方法：**  
1. **创建容器**：需先生成符合 OCI 标准的容器镜像包（包含 `rootfs` 和 `config.json`），可通过 `docker export` 导出镜像。  
2. **运行容器**：支持两种方式：  
   - 直接使用 `runc run` 命令启动容器；  
   - 通过生命周期操作（`create` → `start` → `delete`）分步管理容器。  
3. **Rootless 容器**：支持非特权用户运行容器，需启用内核的用户命名空间（User Namespace）。  

**主要特性：**  
- 支持 `seccomp` 系统调用过滤（依赖 `libseccomp`）；  
- 可通过构建标签（Build Tags）控制功能（如禁用 `seccomp` 或检查点/恢复功能）；  
- 提供测试套件（需 Docker 环境），支持定制化测试用例；  
- 支持与 `systemd` 等进程管理器集成，实现容器自动重启。  

**构建与依赖：**  
需安装 Go 及相关库（如 `libseccomp-dev`），支持通过 `make` 构建和安装。版本号可自定义（`EXTRA_VERSION`），部分功能可通过 `BUILDTAGS` 控制。  

**许可证**：Apache 2.0。