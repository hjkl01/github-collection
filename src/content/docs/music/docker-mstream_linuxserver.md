
---
title: docker-mstream
---

### [linuxserver docker-mstream](https://github.com/linuxserver/docker-mstream)  ![GitHub Repo stars](https://img.shields.io/github/stars/linuxserver/docker-mstream?style=social)

本项目是 LinuxServer.io 提供的 mStream 个人音乐流媒体服务器 Docker 容器。它允许用户将家中电脑的音乐通过 Web 界面（端口 3000）流式传输到任何设备，支持 Android 和 iPhone 移动应用。项目支持 x86-64 和 arm64 架构，基于 Alpine 系统和 s6 覆盖层。v5 版本通过 `config.json` 文件配置，弃用了环境变量设置用户密码的方式，并提供 PUID/PGID 权限映射及定期的应用更新与安全补丁。