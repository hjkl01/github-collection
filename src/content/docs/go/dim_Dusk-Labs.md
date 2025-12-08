
---
title: dim
---

### [Dusk-Labs dim](https://github.com/Dusk-Labs/dim)

Dim 是一款自托管媒体管理工具，可自动整理和美化本地媒体库，支持通过浏览器跨设备访问和播放媒体文件。核心功能包括：

**使用方法**  
1. **二进制安装**：需安装指定系统依赖（如 libva2、ffmpeg 等），下载发布包后解压运行，通过 `http://0.0.0.0:8000` 访问 Web 界面。  
2. **Docker 安装**：通过命令行运行容器，支持配置存储路径和挂载媒体目录，需注意硬件加速需挂载 `/dev/dri/renderD128` 设备。  
3. **源码编译**：需安装 SQLite、Rust（nightly）、Yarn 等依赖，克隆仓库后构建，Linux 需启用 VA-API 硬件加速特性。  

**主要特性**  
- 支持多平台（Linux/其他系统）  
- 提供硬件加速播放（依赖 libva 库）  
- 可扩展挂载多个媒体目录  
- 开源 AGPLv3 协议授权