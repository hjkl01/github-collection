
---
title: ytDownloader
---

### [aandrew-me ytDownloader](https://github.com/aandrew-me/ytDownloader)

**项目核心内容总结：**

**功能**  
ytDownloader 是一款支持数百个网站（如 YouTube、Facebook、TikTok 等）的现代 GUI 视频/音频下载工具，支持下载播放列表、多主题、视频压缩（硬件加速）、字幕选择、范围下载等功能，且无广告和跟踪器。

**使用方法**  
- **Windows**：支持传统安装、Chocolatey、Scoop、Winget 安装；需处理 Windows Defender 防病毒提示。  
- **Linux**：推荐 Flatpak，支持 AppImage 和 Snap 安装。  
- **macOS**：需通过终端移除隔离属性并安装 `yt-dlp`（依赖 Homebrew）。  

**主要特性**  
- 跨平台支持（Linux、Windows、macOS）  
- 视频压缩与硬件加速  
- 多语言支持（含中文、英文、俄语等 20+ 语言）  
- 快速下载与无广告体验  
- 支持字幕、范围下载、播放列表下载  

**技术栈**  
基于 Electron、yt-dlp、ffmpeg 和 Node.js 开发。