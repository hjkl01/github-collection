
---
title: x11docker
---

### [mviereck x11docker](https://github.com/mviereck/x11docker)  ![GitHub Repo stars](https://img.shields.io/github/stars/mviereck/x11docker?style=social)

x11docker 是一个命令行工具，用于在 Docker 或 Podman 容器中运行图形界面（GUI）应用程序及桌面环境。

主要功能包括：
1. **运行容器 GUI**：通过运行独立的 X 服务器或 Wayland 合成器，解决容器缺乏显示服务器的问题，支持单应用无缝模式或完整桌面环境。
2. **安全隔离**：避免 X 安全泄露（不共享宿主 X socket），限制容器权限，默认以非 Root 用户运行，增强沙箱隔离以保护宿主机。
3. **硬件与资源共享**：支持 GPU 硬件加速、音频（PipeWire/PulseAudio）、摄像头、打印机共享及剪贴板互通。
4. **灵活配置**：支持 Linux 及 Windows 环境，可配置网络、文件共享、语言及资源限制，兼容多种后端与初始化系统。
5. **轻量易用**：基于 Bash 脚本，无额外库依赖，安装简便，支持预设配置。