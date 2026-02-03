
---
title: icloud_photos_downloader
---

### [icloud-photos-downloader icloud_photos_downloader](https://github.com/icloud-photos-downloader/icloud_photos_downloader)  ![GitHub Repo stars](https://img.shields.io/github/stars/icloud-photos-downloader/icloud_photos_downloader?style=social)

**项目核心内容总结：**  
iCloud Photos Downloader 是一个跨平台（Linux/Windows/macOS/NAS）的命令行工具，用于从 iCloud 下载照片和视频。支持三种模式：**复制**（仅下载新内容）、**同步**（双向删除差异文件）、**移动**（从 iCloud 删除已下载内容）。主要特性包括支持 Live Photo（分拆为图片和视频）、RAW 格式、自动去重、持续监控 iCloud 变化、增量优化、EXIF 元数据更新等。  

**使用方法：**  
1. 安装方式包括下载可执行文件、通过 Docker/PyPI/AUR/npm 等包管理器安装，或从源码构建。  
2. 同步命令示例：`icloudpd --directory /路径 --username 邮箱 --watch-with-interval 3600`（持续监控 iCloud 变化）。  
3. 授权会话命令：`icloudpd --username 邮箱 --password 密码 --auth-only`（用于验证 2FA 认证）。  

**iCloud 先决条件：**  
需在 iPhone/iPad 上启用 **“iCloud 网络访问”** 并关闭 **“高级数据保护”**，否则会因权限问题导致下载失败。