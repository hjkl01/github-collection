
---
title: docker-libreoffice
---

### [linuxserver docker-libreoffice](https://github.com/linuxserver/docker-libreoffice)  ![GitHub Repo stars](https://img.shields.io/github/stars/linuxserver/docker-libreoffice?style=social)

本项目是 LinuxServer.io 提供的 LibreOffice Docker 容器镜像，旨在通过 Web 浏览器远程运行 LibreOffice 桌面办公套件。
主要功能：
1. **Web 桌面访问**：基于 Selkies 技术，通过 HTTPS（默认端口 3001）在浏览器中提供 LibreOffice 图形界面。
2. **高性能支持**：支持 Wayland 和 X11 模式，兼容 amd64/arm64 架构，支持 GPU 硬件加速及零拷贝编码。
3. **灵活配置**：支持用户权限映射（PUID/PGID）、多语言国际化、持久化应用安装（PRoot）及系统包安装。
4. **安全与运维**：提供基础认证、安全加固选项（禁用终端/Sudo）、GPU 挂载及 Docker-in-Docker 支持，兼容 SealSkin 平台，定期更新补丁。