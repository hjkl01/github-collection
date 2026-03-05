
---
title: aliyundrive-fuse
---

### [messense aliyundrive-fuse](https://github.com/messense/aliyundrive-fuse)  ![GitHub Repo stars](https://img.shields.io/github/stars/messense/aliyundrive-fuse?style=social)

aliyundrive-fuse 是一个基于 FUSE 的阿里云盘挂载工具，可将阿里云盘直接挂载为本地磁盘，主要用于配合 Emby 或 Jellyfin 媒体服务器观看云盘内容，无需通过 WebDAV 或 rclone 进行中转。项目功能特性包括：
1. 仅支持只读模式，不支持写入；
2. 支持 Linux 和 macOS 系统（暂不支持 Windows）；
3. 支持通过命令行配置刷新令牌和挂载点，并支持多种部署方式（pip、snap、预编译包、OpenWrt 等）。