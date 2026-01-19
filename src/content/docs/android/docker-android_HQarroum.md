
---
title: docker-android
---

### [HQarroum docker-android](https://github.com/HQarroum/docker-android)  ![GitHub Repo stars](https://img.shields.io/github/stars/HQarroum/docker-android?style=social)

**项目核心内容总结：**

**功能**  
该项目提供一个基于Alpine的最小化Docker镜像，内置Android模拟器、ADB服务器和KVM加速支持，适用于CI环境，可远程控制（如通过`scrcpy`）。镜像支持自定义Android版本、设备类型及镜像类型（如Google API或Play Store），并可持久化存储数据。

**使用方法**  
- 通过`docker-compose`启动容器（如`docker compose up android-emulator`），或使用`docker build`构建镜像。  
- 支持GPU加速（如`android-emulator-cuda`）及Google Play Store版本（如`android-emulator-cuda-store`）。  
- 运行容器时需挂载`/dev/kvm`设备并映射ADB端口（如`-p 5555:5555`），可通过`adb connect 127.0.0.1:5555`连接。  
- 数据持久化需挂载`/data`目录（如`-v ~/android_avd:/data`）。

**主要特性**  
- 镜像体积优化（如API 33版本压缩后约1.97GB）。  
- 支持通过`API_LEVEL`、`IMG_TYPE`、`ARCHITECTURE`参数自定义构建配置（如API 28 + Play Store）。  
- 可禁用动画、跳过ADB认证等。  
- 支持外部挂载Android SDK以减少镜像体积。  
- 提供Docker Hub预构建镜像（如`halimqarroum/docker-android:api-33`）。