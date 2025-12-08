
---
title: awesome-adb
---

### [mzlogin awesome-adb](https://github.com/mzlogin/awesome-adb)

**核心内容总结：**

**项目功能**  
ADB（Android Debug Bridge）是Android开发调试工具，提供设备连接、日志查看、文件传输、系统操作（如安装/卸载应用、模拟输入事件）、进程管理、网络调试等功能，支持开发、测试和设备管理全流程。

**使用方法**  
1. **基础操作**：通过`adb devices`查看连接设备，`adb logcat`查看日志，`adb install`安装APK，`adb shell`执行设备命令。  
2. **高级功能**：支持端口转发（`adb forward`）、模拟点击/按键（`adb shell input`）、屏幕截图（`adb shell screencap`）、文件传输（`adb push/pull`）。  
3. **调试工具**：结合`dumpsys`分析系统状态，`am`启动Activity，`pm`管理应用包，`uiautomator`进行UI自动化测试。

**主要特性**  
- 跨平台支持（Windows/Linux/macOS）；  
- 支持多设备同时操作；  
- 提供丰富的调试命令（如查看WiFi密码、MAC地址、进程UID等）；  
- 可通过`logcat`过滤日志信息，辅助问题定位；  
- 支持模拟器与真机调试，兼容Android各版本。  

**注意事项**  
- 首次连接需设备授权；  
- 端口占用（如5037端口）可能导致ADB服务异常，需终止冲突进程；  
- 使用`adb kill-server`重置服务可解决部分连接问题。