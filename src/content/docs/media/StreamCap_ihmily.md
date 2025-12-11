
---
title: StreamCap
---

### [ihmily StreamCap](https://github.com/ihmily/StreamCap)

**StreamCap 核心内容总结**：

**项目功能**  
StreamCap 是基于 FFmpeg 和 StreamGet 的多平台直播流录制工具，支持 40+ 国内外主流直播平台（如抖音、TikTok、B站、Twitch 等），提供批量录制、循环监控、定时任务、自动转码为 MP4 等功能。

**主要特性**  
- 支持 Windows/macOS/Linux/Web 端运行  
- 实时监控直播间状态，开播自动录制  
- 支持 TS/FLV/MKV/MOV/MP4 等多种输出格式  
- 录制后自动转码为 MP4  
- 提供直播状态推送通知  

**使用方法**  
1. **预构建程序**：下载对应系统版本（Windows 解压运行 `.exe`，macOS 安装 `.dmg`）。  
2. **源码运行**：需 Python 3.10+，克隆代码后安装依赖，执行 `python main.py`（Linux 需通过 `--web` 参数以 Web 方式运行）。  
3. **Docker 容器**：使用 `docker compose up` 启动，支持后台运行及自定义镜像构建。  

**其他**  
- 需配置 FFmpeg 环境变量（如未预装）。  
- 支持通过 `.env` 文件配置参数（如时区、运行模式）。  
- 提供中文及英文文档，采用 Apache License 2.0 开源协议。