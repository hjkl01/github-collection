
---
title: docker-android
---

### [budtmo docker-android](https://github.com/budtmo/docker-android)  ![GitHub Repo stars](https://img.shields.io/github/stars/budtmo/docker-android?style=social)

Docker-Android 是一款用于 Android 应用开发、构建及测试的 Docker 镜像。

核心功能：
1. **模拟器支持**：内置多种 Android 版本（9.0-14.0）及机型（Samsung、Nexus、Pixel 等）配置。
2. **远程访问**：支持 VNC 查看容器界面，支持 ADB 从外部控制模拟器。
3. **测试与构建**：支持构建 Android 项目，可运行 Appium、Espresso 等 UI 及单元测试。
4. **集成能力**：提供 Web-UI 日志共享，支持集成 Genymotion 云、Jenkins 及主流云服务（Azure、AWS、GCP）。
5. **版本选项**：提供普通版和 Pro 版，Pro 版支持动态代理、无头模式、多语言设置及更高 Android 版本。

运行要求：需安装 Docker 并启用系统虚拟化（KVM）。