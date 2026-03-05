
---
title: aliyundrive-webdav
---

### [messense aliyundrive-webdav](https://github.com/messense/aliyundrive-webdav)  ![GitHub Repo stars](https://img.shields.io/github/stars/messense/aliyundrive-webdav?style=social)

本项目提供阿里云盘 WebDAV 服务，核心功能如下：

1. **视频播放**：支持配合 Infuse、nPlayer 等客户端，在电视等设备上直接播放云盘视频，文件不经服务器中转。
2. **文件传输**：支持通过 WebDAV 协议上传和下载文件（受协议限制不支持秒传）。
3. **多平台部署**：支持 Docker、pip、snap 及 OpenWrt 等多种安装运行方式。
4. **授权方式**：V2 版本基于阿里云盘开放平台接口，支持扫码或在线工具获取 refresh token。
5. **配置灵活**：支持命令行配置端口、认证用户、缓存大小及传输缓冲等参数。