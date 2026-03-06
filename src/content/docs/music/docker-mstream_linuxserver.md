
---
title: docker-mstream
---

### [linuxserver docker-mstream](https://github.com/linuxserver/docker-mstream)  ![GitHub Repo stars](https://img.shields.io/github/stars/linuxserver/docker-mstream?style=social)

本项目是 LinuxServer.io 提供的 mStream 个人音乐流媒体服务器的 Docker 镜像。

**功能概述：**
允许用户在家庭电脑上托管音乐库，并通过 Web 界面或移动应用（Android/iPhone）将音乐流式传输到任意设备。

**技术特性：**
- 支持 x86-64 和 arm64 架构。
- 包含定期应用更新、安全更新及基础系统更新。
- 采用 s6 overlay 管理容器，支持 PUID/PGID 权限映射。
- Web 管理界面默认端口为 3000。

**使用说明：**
- 支持 Docker Compose 和 Docker CLI 部署。
- 配置文件和音乐目录分别挂载至 `/config` 和 `/music`。
- v5 版本需通过 `config.json` 管理配置，不再支持通过环境变量设置用户密码。