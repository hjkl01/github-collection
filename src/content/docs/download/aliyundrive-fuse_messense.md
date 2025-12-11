
---
title: aliyundrive-fuse
---

### [messense aliyundrive-fuse](https://github.com/messense/aliyundrive-fuse)

aliyundrive-fuse 是一个将阿里云盘挂载为本地磁盘的 FUSE 工具，主要用于配合 Emby 或 Jellyfin 播放云盘视频内容。核心特性包括：  
1. **仅支持读取**，不支持写入操作；  
2. 支持 **Linux 和 macOS**，不支持 Windows；  
3. 直接通过 FUSE 挂载，无需依赖 WebDAV 或 rclone 中转。  

**安装方式**：  
- Linux 需安装 fuse3，macOS 需安装 macfuse；  
- 可通过 pip、Snapcraft 或 OpenWrt 的 ipk 文件安装。  

**使用方法**：  
1. 创建挂载目录，执行命令挂载，需指定刷新令牌（`--refresh-token`）和挂载路径；  
2. Docker 环境下需将挂载路径映射到容器内（如 Jellyfin 的 `/media` 路径）。  

**适用场景**：  
直接作为 Emby/Jellyfin 的媒体库路径，或通过 Docker 容器访问云盘文件。