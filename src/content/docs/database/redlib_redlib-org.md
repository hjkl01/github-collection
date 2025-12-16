
---
title: redlib
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/redlib-org/redlib?style=social) ](https://github.com/redlib-org/redlib)
### [redlib-org redlib](https://github.com/redlib-org/redlib)

**项目核心内容总结：**  
Redlib 是一个可高度自定义的 Reddit 前端替代应用，支持以下功能：  
- **自定义设置**：主题（如暗黑、亮色）、布局（卡片式、紧凑式）、内容过滤（NSFW 隐藏/模糊）、视频自动播放等。  
- **部署方式**：支持 Docker、Heroku、Replit 等平台快速部署，亦可通过源码编译安装。  
- **配置管理**：通过环境变量（如 `REDLIB_DEFAULT_THEME=dark`）或 `redlib.toml` 配置文件调整默认参数，支持多实例独立配置（如端口、Pushshift 链接）。  
- **特性扩展**：支持 RSS 订阅、HLS 视频流、去除默认推荐频道等功能。  

**使用方法**：  
1. **部署**：使用 Docker 命令（`docker run`）或 Compose 文件启动，或通过 Heroku/Replit 等平台一键部署。  
2. **配置**：修改 `.env` 文件或 `redlib.toml` 设置默认主题、端口等参数。  
3. **运行**：通过命令行参数（如 `-p 8080` 指定端口）启动服务。