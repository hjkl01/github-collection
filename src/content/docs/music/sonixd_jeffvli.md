
---
title: sonixd
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/jeffvli/sonixd?style=social) ](https://github.com/jeffvli/sonixd)
### [jeffvli sonixd](https://github.com/jeffvli/sonixd)

**项目核心内容总结：**  

**项目功能：**  
Sonixd 是一款跨平台桌面客户端，支持 Subsonic-API 及 Jellyfin（0.8.0+）兼容的音乐服务器（如 Navidrome、Airsonic、Gonic、Astiga 等）。提供播放列表管理、拖拽排序、跨平台媒体键控制等功能。  

**主要特性：**  
- 支持 HTML5 音频播放（含淡入淡出、无间隙播放）  
- 大型播放列表与队列管理  
- 多主题界面  
- 兼容多种音乐服务器（含 Jellyfin）  
- 基于 Electron、React 和 rsuite 组件库开发  

**使用方法：**  
1. 从 [GitHub 发布页](https://github.com/jeffvli/sonixd/releases) 下载对应系统的安装包。  
2. **Windows**：使用 `winget install sonixd` 或 [scoop](https://scoop.sh) 安装。  
3. **MacOS**：通过 `brew install --cask sonixd` 安装。  
4. **Linux**：Arch 用户可从 AUR 安装。  
5. 启动后输入服务器地址、用户名及密码登录（如使用 Airsonic-Advanced 需创建 decodable 账户）。  

**项目状态：**  
当前版本 0.15.4 进入维护模式，仅修复严重漏洞，新功能开发已转向 [Feishin](https://github.com/jeffvli/feishin) 项目。