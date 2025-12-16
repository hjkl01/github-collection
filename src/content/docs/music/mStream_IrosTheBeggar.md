
---
title: mStream
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/IrosTheBeggar/mStream?style=social) ](https://github.com/IrosTheBeggar/mStream)
### [IrosTheBeggar mStream](https://github.com/IrosTheBeggar/mStream)

**mStream Music 核心内容总结：**

**项目功能**  
mStream 是一款个人音乐流媒体服务器，支持将本地音乐库通过网络传输至任意设备，实现跨平台播放。WebApp 支持无缝播放、Milkdrop 可视化效果、播放列表共享及网页端文件上传功能。

**使用方法**  
- **安装方式**：提供 Docker 镜像、跨平台二进制文件、源码编译及 AWS Terraform 部署方案。  
- **快速安装**：通过 CLI 命令克隆仓库并运行 `npm run-script wizard` 自动配置。  

**主要特性**  
- **跨平台兼容**：支持 Windows、macOS、Linux、FreeBSD 及 ARM 设备（如树莓派）。  
- **高效性能**：低资源占用，适配超大容量音乐库（多TB级）。  
- **技术依赖**：基于 NodeJS v10+，支持 FLAC、MP3、WAV 等主流音频格式。  

**开源贡献**  
依赖开源库（如音乐元数据解析器、LokiJS 数据库、Butterchurn 可视化器），并由 LinuxServer.io 维护 Docker 镜像。