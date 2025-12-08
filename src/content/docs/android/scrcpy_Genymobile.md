
---
title: scrcpy
---

### [Genymobile scrcpy](https://github.com/Genymobile/scrcpy)

**项目核心内容总结：**  
scrcpy 是一款通过 USB 或 TCP/IP 连接 Android 设备的开源工具，可实时镜像设备屏幕与音频，并通过电脑键盘、鼠标控制设备，无需 Root 或安装应用。支持 Linux、Windows、macOS 系统。  

**主要功能：**  
- 屏幕与音频镜像，支持无线连接；  
- 高性能（30~120fps）、低延迟（35~70ms）、高清画质（1920×1080 及以上）；  
- 支持音频转发（Android 11+）、屏幕录制、虚拟显示、摄像头镜像（Android 12+）、作为网络摄像头（Linux）、物理键盘/鼠标模拟、游戏手柄控制、OTG 模式等；  
- 无广告、无互联网依赖，完全免费开源。  

**使用方法：**  
- 安装对应系统版本（Linux/Windows/macOS）；  
- 常用命令如：`scrcpy -m1024`（调整分辨率）、`scrcpy --record=file.mp4`（录制视频）、`scrcpy --otg`（OTG 模式控制设备）；  
- 鼠标操作：右键触发返回键，中键触发主页键，Alt+F 切换全屏。  

**注意事项：**  
- Android 设备需 API 21（5.0）以上，音频转发需 Android 11 及以上；  
- 部分设备（如小米）需启用“USB 调试（安全设置）”以支持键盘/鼠标控制；  
- OTG 模式无需 USB 调试。