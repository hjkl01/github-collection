
---
title: Jellyfin-Enhanced
---

### [n00bcodr Jellyfin-Enhanced](https://github.com/n00bcodr/Jellyfin-Enhanced)

**Jellyfin Enhanced 核心内容总结：**  
Jellyfin Enhanced 是一个增强 Jellyfin Web UI 功能的插件，提供自定义键盘快捷键、Jellyseerr 集成（用于请求媒体）、TMDB 数据获取（如影片简介）、Elsewhere 功能（显示其他平台资源）、暂停屏幕信息展示、设置面板等特性。支持官方 Jellyfin Web、Android 和 iOS 客户端，但不兼容第三方应用或 Android TV 等非嵌入式 Web UI 平台。  

**使用方法：**  
通过插件安装后，可通过侧边栏菜单或快捷键 `?` 打开增强面板，自定义快捷键、管理 Jellyseerr 设置、查看影片信息等。  

**关键特性：**  
- 多平台兼容：支持官方 Web、移动端，但不支持 Android TV 等。  
- 集成功能：Jellyseerr 请求、TMDB 数据、Elsewhere 资源展示。  
- 自定义设置：键盘快捷键、暂停屏幕内容、插件语言（自动适配用户语言）。  
- 安装注意事项：Docker 用户需正确配置 `index.html` 路径，Windows 用户需设置 Jellyfin 文件夹权限，Jellyfin 10.11 版本需检查任务触发器。  

**常见问题：**  
安装失败可能因权限不足或路径配置错误，网络问题可能导致数据加载失败，需检查 TMDB 或 Jellyseerr 的连接状态。  

**许可证：** MIT 开源协议。