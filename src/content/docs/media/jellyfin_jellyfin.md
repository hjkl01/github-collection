
---
title: jellyfin
---

### [jellyfin jellyfin](https://github.com/jellyfin/jellyfin)

**Jellyfin 核心内容总结：**  

**项目功能**  
Jellyfin 是一个开源的媒体管理系统，支持用户本地媒体的管理和跨设备流媒体播放，替代 Emby 和 Plex。其后端基于 .NET 平台开发，实现跨平台兼容性。  

**主要特性**  
- 完全免费，无付费功能或隐藏条款；  
- 支持多平台（Windows、Linux、macOS 等，不包括 FreeBSD）；  
- 提供 Web 界面及多端应用支持；  
- 社区驱动，支持翻译、功能建议和代码贡献；  
- 提供 Docker 镜像及详细文档。  

**使用方法**  
1. **安装**：通过官网下载预编译包，或从源码构建（需 .NET 9.0 SDK、ffmpeg 及 jellyfin-web 前端文件）；  
2. **运行**：使用 Visual Studio/Visual Studio Code 或命令行（如 `dotnet run`）启动服务，默认访问地址为 `http://localhost:8096`；  
3. **开发**：支持单元测试（`dotnet test`）、GitHub Codespaces 环境配置及分离前端部署模式（通过 `--nowebclient` 参数）。  

**其他**  
- 支持通过 API 文档（`/api-docs`）调试接口；  
- 社区提供 DigitalOcean 和 JetBrains 等技术支持。