
---
title: FaceWinUnlock-Tauri
---

### [zs1083339604 FaceWinUnlock-Tauri](https://github.com/zs1083339604/FaceWinUnlock-Tauri)  ![GitHub Repo stars](https://img.shields.io/github/stars/zs1083339604/FaceWinUnlock-Tauri?style=social)

FaceWinUnlock-Tauri 是一款基于 Tauri 框架的 Windows 面容识别解锁增强软件。它通过向登录界面注入自定义 DLL，结合 Vue 3 前端与 OpenCV 算法，提供类似 Windows Hello 的刷脸解锁体验。

主要功能：
- 系统支持 Windows 10/11，兼容本地及微软账户。
- 集成 2D 面容识别与活体检测，支持多面容、多账户管理。
- 数据本地 SQLite 存储，不上传云端，支持静默自启及解锁重试。
- 提供系统初始化向导及组件卸载功能。

注意事项：涉及系统底层修改，存在登录故障风险；仅支持账户密码（不支持 Pin 码）；因 2D 识别技术存在安全绕过风险，建议仅用于个人家用环境。