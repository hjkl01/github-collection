
---
title: docker-android
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/budtmo/docker-android?style=social) ](https://github.com/budtmo/docker-android)
### [budtmo docker-android](https://github.com/budtmo/docker-android)

**项目核心内容总结：**  
Docker-Android 是一个基于 Docker 的镜像，专为 Android 开发和测试设计，支持原生、Web 和混合应用的开发。其核心功能包括：  
1. **多设备模拟器**：支持多种设备型号（如 Samsung Galaxy 系列、Nexus 系列、Pixel C 等）和不同 Android 版本（9.0 至 14.0 及 Genymotion 云集成）。  
2. **可视化与控制**：通过 VNC 实时查看容器内操作，支持通过 ADB 连接远程控制模拟器，提供 Web 界面查看日志。  
3. **云集成与构建**：兼容 Genymotion 云服务，支持 Android 项目构建及 Appium、Espresso 等测试框架的 UI 测试。  
4. **数据持久化**：通过挂载卷实现容器重启后数据保留。  

**使用方法**：  
- 确保系统支持虚拟化（如 Ubuntu），安装 Docker。  
- 使用 `docker run` 命令启动容器，指定设备型号、端口映射及必要参数（如 `-e EMULATOR_DEVICE="Samsung Galaxy S10"`）。  
- 通过 `http://localhost:6080` 访问 Web 界面，查看模拟器状态及日志。  

**主要特性**：  
- 提供多种 Android 版本镜像（如 `budtmo/docker-android:emulator_11.0`）。  
- 支持 Windows 11 下 WSL2 的硬件加速配置。  
- 包含多个使用场景文档（如构建项目、Jenkins 集成、云部署等）。  
- 有 Pro 版本（需赞助），提供代理设置、多语言支持、新 Android 版本、资源优化等功能。