
---
title: jellyfin-desktop
---

### [jellyfin jellyfin-desktop](https://github.com/jellyfin/jellyfin-desktop)  ![GitHub Repo stars](https://img.shields.io/github/stars/jellyfin/jellyfin-desktop?style=social)

**Jellyfin Desktop 核心内容总结**  

**项目功能**  
Jellyfin Desktop 是 Jellyfin 的桌面客户端，基于 jellyfin-web 开发，内置 MPV 播放器，支持 Windows、macOS 和 Linux 系统。与传统 Jellyfin Desktop 不同，媒体内容在同一个窗口内通过 jellyfin-web 界面播放，支持音频直通功能。  

**使用方法**  
- **下载安装**：提供 Windows、macOS、Linux 的安装包下载链接，Linux 用户也可通过 Flathub 安装。  
- **构建方式**：支持跨平台构建，提供 Linux（Ubuntu/Fedora）、Windows 和 macOS 的详细构建步骤，需安装依赖库（如 MPV、Qt、CMake 等）。  

**主要特性**  
1. **跨平台支持**：兼容 Windows、macOS 和 Linux 系统。  
2. **嵌入式播放器**：使用 MPV 实现媒体播放，支持音频直通。  
3. **配置与调试**：提供日志文件路径（各平台不同）、配置文件（`jellyfin-desktop.conf` 和 `mpv.conf`）存储位置，支持通过 `--remote-debugging-port` 参数启用浏览器开发者工具调试。  
4. **开源授权**：采用 GPL v2 许可证，依赖库许可证信息可运行时通过 `--licenses` 参数查看。  

**注意事项**  
- 构建 MPV 时需禁用 Pipewire 以避免崩溃。  
- macOS 版本需注意 Intel 和 Apple Silicon 的系统兼容性要求。