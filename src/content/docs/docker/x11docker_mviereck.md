
---
title: x11docker
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/mviereck/x11docker?style=social) ](https://github.com/mviereck/x11docker)
### [mviereck x11docker](https://github.com/mviereck/x11docker)

**项目功能：**  
x11docker 是一个基于 Docker 的工具，用于在容器中运行图形界面应用程序和桌面环境。它支持多种桌面环境（如 KDE、GNOME、XFCE 等），并可以与硬件加速、声音共享、文件共享等功能结合使用。

**使用方法：**  
通过命令行使用 `x11docker` 命令运行容器，可指定桌面环境、共享文件夹、启用 GPU 加速、设置 PulseAudio 声音等。用户还可以通过自定义 Dockerfile 添加应用，构建专属镜像。

**主要特性：**  
- 支持多种桌面环境和图形应用；
- 提供 GPU 加速、声音共享、文件共享等功能；
- 可自定义镜像，支持持久化配置；
- 项目提供了一系列示例镜像，方便用户快速使用；
- 支持多种 Linux 发行版和轻量级系统（如 Alpine、Void Linux）。

---

**核心内容总结：**  
x11docker 是一个用于在 Docker 容器中运行图形界面应用程序和桌面环境的工具，支持多种桌面环境和图形应用，提供 GPU 加速、声音共享、文件共享等功能。用户可通过命令行快速启动容器，并通过自定义 Dockerfile 扩展功能。项目提供多个示例镜像，适用于开发、测试和演示等多种场景。