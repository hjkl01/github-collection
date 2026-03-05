
---
title: docker-webtop
---

### [linuxserver docker-webtop](https://github.com/linuxserver/docker-webtop)  ![GitHub Repo stars](https://img.shields.io/github/stars/linuxserver/docker-webtop?style=social)

Webtop 是 LinuxServer.io 提供的一个 Docker 容器项目，允许用户通过现代 Web 浏览器访问完整的桌面环境。

**主要功能：**
1. **多系统支持**：基于 Alpine、Ubuntu、Fedora、Arch、Debian 等系统，提供 XFCE、KDE、MATE、i3 等桌面/窗口管理器。
2. **Web 访问**：通过 HTTPS 协议（默认端口 3001）在浏览器中运行桌面，支持 x86-64 和 arm64 架构。
3. **硬件加速**：支持 Wayland 模式及 GPU 硬件加速（Intel、AMD、Nvidia），利用零拷贝技术降低 CPU 占用和延迟。
4. **应用管理**：支持通过 PRoot 实现应用的持久化保存，或基于系统仓库安装临时应用。
5. **安全与配置**：提供用户权限映射、多语言支持、安全加固选项，建议配合反向代理使用以保障互联网访问安全。