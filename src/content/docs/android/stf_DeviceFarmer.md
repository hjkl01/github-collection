
---
title: stf
---

### [DeviceFarmer stf](https://github.com/DeviceFarmer/stf)  ![GitHub Repo stars](https://img.shields.io/github/stars/DeviceFarmer/stf?style=social)

STF (Smartphone Test Farm) 是一款基于 Web 的远程 Android 设备调试与管理平台。

主要功能：
1. **远程控制**：支持通过浏览器实时查看屏幕（最高 30-40 FPS）、触控操作、键盘输入、APK 安装与启动、端口转发、Shell 命令执行、日志查看及文件管理。
2. **兼容性与连接**：支持 Android 2.3.3 至 15 及 Wear OS 等系统，无需 Root 权限；支持通过 `adb connect` 远程调试，兼容 Android Studio 等 IDE。
3. **资源管理**：提供设备库存监控（状态、电量、硬件信息）、预订与分区系统（按项目/时间分配设备）、用户及设备管理功能。
4. **扩展性**：支持简单的 REST API。

注：系统目前安全性较低，主要面向内部可信环境使用。