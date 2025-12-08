
---
title: spotify-downloader
---

### [spotDL spotify-downloader](https://github.com/spotDL/spotify-downloader)

**核心内容总结：**

spotDL 是一款命令行音乐下载工具，可从 Spotify 播放列表中搜索 YouTube 歌曲并下载，同时支持专辑封面、歌词和元数据的获取。  

**主要功能：**  
- 通过 Spotify 链接下载 YouTube 音乐，支持高音质（普通用户 128kbps，YouTube Music 用户 256kbps）。  
- 提供多种操作模式，如下载（`download`）、同步目录（`sync`）、保存元数据（`save`）、生成歌曲链接（`url`）等。  
- 支持通过 Python 安装（`pip install spotdl`）、预编译文件、Docker 容器等多种方式部署。  

**使用方法：**  
1. 安装 FFmpeg（系统级或通过 `spotdl --download-ffmpeg` 自动安装）。  
2. 基础命令：`spotdl [操作] [参数] [Spotify 链接]`，例如 `spotdl download https://spotify.link`。  
3. 高级功能：使用 `sync` 同步播放列表与本地目录，或通过 `web` 启动简易网页界面。  

**特性：**  
- 依赖 YouTube 作为音乐源，避免 Spotify 下载限制。  
- 支持跨平台（Windows、macOS、Linux、Termux）。  
- 开源 MIT 许可证，社区贡献活跃。