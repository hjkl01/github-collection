
---
title: redroid-doc
---

### [remote-android redroid-doc](https://github.com/remote-android/redroid-doc)

语句通顺，准确，简洁，符合中文表达习惯，没有语法错误。
</think>

### 项目核心内容总结

**项目功能**  
redroid 是一个基于 GPU 加速的 Android In Cloud（AIC）解决方案，允许在 Linux 主机（如 Docker、Podman、Kubernetes 等）中运行多个 Android 实例。它适用于云游戏、手机虚拟化、自动化测试等场景。

**使用方法**  
- 可通过 Docker 快速启动，支持多种 Linux 发行版（如 Ubuntu 20.04）。
- 安装 Docker 和必要的内核模块后，使用 `docker run` 命令启动 redroid 容器，并通过 ADB 和 scrcpy 查看和控制 Android 界面。
- 可自定义显示参数（如分辨率、FPS、DPI）、网络设置、GPU 渲染模式等。

**主要特性**  
- 支持 Android 8.1 至 Android 16 的多个版本（包括 64 位版本）。
- 提供 Native Bridge 支持，可在 x86 实例中运行 ARM 应用。
- 支持 GMS（Google Mobile Services）通过 Open GApps、MicroG 等方案。
- 支持 WebRTC 流媒体传输（计划中）。
- 提供详细的配置项，如 DNS 设置、代理配置、GPU 加速模式等。
- 提供构建和调试工具，便于扩展和定制。

**注意事项**  
- 不建议在公网暴露 ADB 端口，以防止容器或主机被入侵。
- 部分功能（如 WebRTC）尚在开发阶段。