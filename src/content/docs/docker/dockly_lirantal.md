
---
title: dockly
---

### [lirantal dockly](https://github.com/lirantal/dockly)

**核心内容总结：**  
Dockly 是一个用于管理 Docker 容器、服务和镜像的沉浸式终端工具，提供直观的界面和丰富的功能。  

**功能与特性：**  
- 支持本地和远程 Docker 守护进程连接（通过 Unix Socket 或远程主机/端口/协议）。  
- 可通过 `--containerFilters` 参数按名称、状态等条件过滤容器。  
- 提供命令行选项自定义连接参数（如 `-s` 指定 Socket 路径，`-H` 指定远程主机）。  
- 支持通过 Docker 镜像运行（需挂载 `/var/run/docker.sock`）。  

**使用方法：**  
1. **安装**：使用 `npm install -g dockly` 全局安装，或通过 Docker 命令运行镜像。  
2. **启动**：直接运行 `dockly` 连接本地 Docker 守护进程，或通过参数指定远程连接。  
3. **过滤容器**：如 `--containerFilters="name=test&status=running"` 过滤运行中的 `test` 容器。  

**兼容性要求：**  
需 Node.js v7.6 及以上版本，部分功能依赖 UTF-8 编码环境。