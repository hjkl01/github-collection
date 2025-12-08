
---
title: compose
---

### [docker compose](https://github.com/docker/compose)

**Docker Compose 核心内容总结：**  

**项目功能**  
Docker Compose 是一个用于定义和运行多容器 Docker 应用的工具，通过 `Compose 文件格式`（如 `compose.yaml`）配置应用环境，支持一键启动整个应用（`docker compose up`）。  

**使用方法**  
1. 用 `Dockerfile` 定义应用环境；  
2. 用 `compose.yaml` 定义服务及依赖（如端口映射、卷挂载）；  
3. 执行 `docker compose up` 启动应用。  

**主要特性**  
- 支持最新 Compose 文件格式，兼容 Docker Swarm（但 Swarm 未完全适配新特性）；  
- Windows/macOS 用户可通过 Docker Desktop 直接使用；Linux 用户需手动下载二进制文件并安装；  
- 提供版本管理（v2 为当前主版本，v1 为 Python 实现的旧版本分支）。