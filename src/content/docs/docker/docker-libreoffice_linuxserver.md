
---
title: docker-libreoffice
---

### [linuxserver docker-libreoffice](https://github.com/linuxserver/docker-libreoffice)  ![GitHub Repo stars](https://img.shields.io/github/stars/linuxserver/docker-libreoffice?style=social)

这是一个基于 LinuxServer.io 的 LibreOffice Docker 容器镜像，允许用户通过 Web 浏览器远程使用 LibreOffice 办公套件。项目支持 x86-64 和 arm64 架构，基于 Selkies 框架构建桌面流媒体功能，并支持 Wayland 模式以实现 GPU 硬件加速（零拷贝编码）及降低延迟。核心特性包括强制 HTTPS 传输、用户权限映射（PUID/PGID）、支持 PRoot 方式实现应用持久化、以及通过环境变量灵活配置语言、端口和硬件加速参数。项目提供安全加固选项（如禁用终端和 sudo），并兼容 SealSkin 平台，默认通过 HTTPS 3001 端口访问，建议置于可信网络或反向代理后端以保障安全。