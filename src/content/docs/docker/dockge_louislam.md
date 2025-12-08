
---
title: dockge
---

### [louislam dockge](https://github.com/louislam/dockge)

**项目核心内容总结：**  

**功能：**  
Dockge 是一款自托管的 Docker Compose 堆栈管理工具，支持创建/编辑/启动/停止/重启/删除堆栈、更新镜像、交互式编辑 Compose 文件、Web 终端、多 Docker 主机管理（1.4.0 新增）、将 `docker run` 命令转换为 Compose 文件。文件存储在本地，可直接使用 `docker compose` 命令操作。  

**使用方法：**  
需安装 Docker 20+ 或 Podman（仅 Podman 需额外安装 `podman-docker`）。默认堆栈目录为 `/opt/stacks`，默认端口 5001。基本安装步骤为：创建目录、下载 Compose 文件、执行 `docker compose up -d`。高级用户可通过 URL 自定义端口和堆栈路径。更新时执行 `docker compose pull && docker compose up -d`。  

**主要特性：**  
- 实时响应（如镜像拉取、容器启动状态）  
- 基于文件的本地存储，不强制迁移文件  
- 支持多 Docker 主机管理  
- 类似 Uptime Kuma 的美观 UI  
- 交互式编辑器和 Web 终端  
- 支持将 `docker run` 转换为 Compose 文件