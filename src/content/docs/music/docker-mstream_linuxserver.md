
---
title: docker-mstream
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/linuxserver/docker-mstream?style=social) ](https://github.com/linuxserver/docker-mstream)
### [linuxserver docker-mstream](https://github.com/linuxserver/docker-mstream)

**项目功能**：  
mStream 是一个基于 Docker 的音乐流媒体服务器，支持通过 Web 界面管理音乐库和播放列表，用户可自定义配置文件路径、端口映射及权限设置。

**使用方法**：  
1. **Docker Compose**：通过 `docker-compose.yml` 文件定义容器参数，如端口映射（`-p 3000:3000`）、用户权限（`PUID=1000`, `PGID=1000`）及配置目录（`-v /config`）。  
2. **Docker CLI**：使用 `docker run` 命令直接运行容器，参数与 Compose 类似，需手动指定端口、卷挂载及环境变量。  

**主要特性**：  
- **灵活配置**：支持通过环境变量（如 `TZ` 设置时区、`UMASK` 调整文件权限）和卷挂载（`/music` 存储音乐文件，`/config` 存储配置）定制化部署。  
- **用户权限管理**：通过 `PUID` 和 `PGID` 确保容器与主机文件权限一致，避免因权限问题导致的配置异常。  
- **日志与监控**：提供实时日志查看（`docker logs -f`）和容器版本查询（`docker inspect`）。  
- **更新支持**：支持通过 `docker-compose pull` 或 `docker pull` 更新镜像，并通过 `docker-compose up -d` 或 `docker rm` 重建容器。  
- **版本兼容性**：基于 Alpine Linux 构建，历史版本记录包括 Alpine 升级（如 3.10 至 3.20）、弃用 armhf 架构、迁移至 s6v3 等。  

**注意事项**：  
- mStream v5 后版本需通过 `config.json` 配置用户密码，弃用 `USER`、`PASSWORD` 环境变量。  
- 镜像更新需重建容器，不建议在容器内直接更新应用。