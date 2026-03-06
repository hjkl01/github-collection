
---
title: docker-headless-vnc-container
---

### [ConSol docker-headless-vnc-container](https://github.com/ConSol/docker-headless-vnc-container)  ![GitHub Repo stars](https://img.shields.io/github/stars/ConSol/docker-headless-vnc-container?style=social)

该项目提供包含“无头”VNC 会话的 Docker 镜像，用于实现远程图形化桌面访问。

- **环境组件**：集成 Xfce4 或 IceWM 桌面环境、VNC 服务器（默认端口 5901）、noVNC HTML5 网页客户端（默认端口 6901）及 Firefox 和 Chromium 浏览器。
- **系统镜像**：基于 Rocky 9 和 Debian 11 操作系统，提供多种桌面窗口管理器组合。
- **部署支持**：支持 Docker 容器运行，兼容 Kubernetes 和 OpenShift 等容器编排平台。
- **配置与扩展**：支持自定义 VNC 分辨率、密码及用户权限；允许通过自定义 Dockerfile 扩展软件；支持开启只读模式；可调整共享内存以优化浏览器性能。