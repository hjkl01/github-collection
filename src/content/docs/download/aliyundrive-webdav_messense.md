
---
title: aliyundrive-webdav
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/messense/aliyundrive-webdav?style=social) ](https://github.com/messense/aliyundrive-webdav)
### [messense aliyundrive-webdav](https://github.com/messense/aliyundrive-webdav)

**项目核心内容总结：**

**功能**  
将阿里云盘转换为WebDAV服务，支持通过Infuse、nPlayer等客户端直接访问云盘视频，无需服务器中转；支持文件上传（不支持秒传）。V2版本基于阿里云盘开放平台接口，不兼容旧版refresh token及梅林固件（需付费支持）。

**使用方法**  
1. **安装**：通过pip、snap、OpenWrt的ipk包或Docker安装。Docker需配置`REFRESH_TOKEN`、用户名密码等环境变量。  
2. **配置**：通过扫码或在线工具获取阿里云盘的`refresh_token`；支持命令行参数设置端口、认证、缓存、上传策略等（如`--skip-upload-same-size`）。  
3. **高级用法**：推荐rclone使用Nextcloud模式并配合`--no-update-modtime`参数，避免重复上传。

**主要特性**  
- 支持WebDAV协议，兼容主流媒体播放器；  
- 自动生成索引文件，优化目录缓存；  
- 支持TLS加密（部分架构受限）；  
- 可配置读写模式、上传缓冲区大小；  
- 提供Docker镜像及OpenWrt插件支持。  

**限制**  
- V2版本不兼容旧版refresh token及梅林固件；  
- TLS/HTTPS不支持MIPS架构；  
- `--skip-upload-same-size`可能跳过修改后的同大小文件。