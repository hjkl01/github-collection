
---
title: FaceWinUnlock-Tauri
---

### [zs1083339604 FaceWinUnlock-Tauri](https://github.com/zs1083339604/FaceWinUnlock-Tauri)  ![GitHub Repo stars](https://img.shields.io/github/stars/zs1083339604/FaceWinUnlock-Tauri?style=social)

**项目核心内容总结：**  
FaceWinUnlock-Tauri 是一款基于 Tauri 框架开发的 Windows 面容识别解锁工具，通过自定义 Credential Provider（DLL）注入系统登录界面，结合 Vue 3 前端与 OpenCV 人脸识别算法，实现类似 Windows Hello 的解锁体验。支持多账户解锁、面容录入、静默自启等功能，适用于 Windows 10/11 64 位系统。

**使用方法：**  
1. 运行软件后完成系统初始化（自动检测摄像头权限及注册表环境）；  
2. 通过首选项选择摄像头设备，录入面容并关联账户；  
3. 使用 `Win + L` 锁定屏幕后，通过摄像头进行面容识别解锁；  
4. 卸载时需通过软件内卸载核心组件，并执行安装目录的 `uninstall.exe`。

**主要特性：**  
- 现代化 UI（Vue 3 + Element Plus）；  
- 系统级集成（自定义 Credential Provider DLL）；  
- 支持本地账户与微软联机账户；  
- 轻量级 Rust 后端保障性能与安全性；  
- 面容数据本地存储（SQLite），不上传云端。

**注意事项：**  
- 涉及注册表修改与 Winlogon 进程操作，存在系统登录异常风险；  
- 仅支持 2D 面容识别，存在被照片/视频绕过的安全隐患；  
- 不支持 Pin 码解锁，需输入账户密码；  
- 严禁用于高安全性环境（如办公或服务器）。  

**技术栈：**  
前端（Vue 3、Pinia、Element Plus）、后端（Rust、Tauri）、数据库（SQLite 3）、人脸识别（OpenCV）、系统组件（WinLogon Credential Provider DLL）。