### [messense aliyundrive-webdav](https://github.com/messense/aliyundrive-webdav)  ![GitHub Repo stars](https://img.shields.io/github/stars/messense/aliyundrive-webdav?style=social)

本项目是一个阿里云盘 WebDAV 服务。主要功能如下：

1. **直接访问云盘**：支持 Infuse、nPlayer 等支持 WebDAV 协议的客户端直接访问阿里云盘，实现在电视等设备上流媒体播放，文件不经过服务器中转。
2. **文件操作**：支持文件上传，但受 WebDAV 协议限制不支持秒传。
3. **多端部署**：提供 Docker、pip、Snap、OpenWrt 路由器及二进制包等多种安装与运行方式。
4. **服务管理**：提供命令行工具，支持扫码授权获取刷新令牌（refresh token）及自定义 WebDAV 服务配置参数。