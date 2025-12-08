
---
title: sen
---

### [TomasTomecek sen](https://github.com/TomasTomecek/sen)

**项目核心内容总结：**  

**功能**：`sen` 是一个用于管理 Docker 容器和镜像的终端用户界面工具，支持容器/镜像的启动、停止、删除、日志查看、实时更新、空间占用统计等功能，并提供类似 `docker images --tree` 的镜像树视图。  

**主要特性**：  
- 支持 Vim 风格快捷键（如 `j/k` 移动、`/` 搜索等）；  
- 实时同步 Docker 状态（如其他终端拉取镜像时自动更新）；  
- 提供容器/镜像的详细信息查看、日志流式输出；  
- 支持过滤、搜索、多缓冲区导航；  
- 可通过 `:df` 查看磁盘使用情况。  

**使用方法**：  
1. **Docker 安装**：拉取镜像 `tomastomecek/sen`，并挂载 Docker 套接字 `/var/run/docker.sock`；  
2. **PyPI 安装**：通过 `pip3 install sen` 安装，需先安装依赖 `urwidtrees`；  
3. **Git 安装**：克隆仓库后使用 `pip3` 安装依赖并运行；  
4. **Podman 支持**：通过设置 `DOCKER_HOST` 指向 Podman 的 Unix 套接字路径启动。  

**注意事项**：  
- 项目处于维护模式，仅修复 bug，不新增功能；  
- 需确保 Docker 或 Podman 的 Unix 套接字可访问；  
- SELinux 系统需在挂载时添加 `:Z` 标志。