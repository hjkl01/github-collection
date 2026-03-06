
---
title: stf
---

### [DeviceFarmer stf](https://github.com/DeviceFarmer/stf)  ![GitHub Repo stars](https://img.shields.io/github/stars/DeviceFarmer/stf?style=social)

STF（Smartphone Test Farm）是一个基于 Web 的远程移动设备测试与管理平台，支持通过浏览器调试和控制 Android 手机、智能手表及其他智能设备。核心功能包括实时屏幕查看（30-40 FPS）、远程触控与输入、APK 安装、端口转发、Shell 命令执行、文件管理及设备日志监控。平台提供设备库存监控、状态查询及资源调度系统（支持设备分组、用户预约与权限管理）。集成 ADB 远程连接与调试工具支持，并提供 REST API。项目基于 Node.js 开发，需 ADB、RethinkDB 等依赖，支持 Docker 部署，内部通信未加密，适用于可信测试环境。