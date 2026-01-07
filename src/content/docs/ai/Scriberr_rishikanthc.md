
---
title: Scriberr
---

### [rishikanthc Scriberr](https://github.com/rishikanthc/Scriberr)  ![GitHub Repo stars](https://img.shields.io/github/stars/rishikanthc/Scriberr?style=social)

**项目核心内容总结：**

**功能**  
Scriberr 是一个支持语音转文字、说话人识别（Diarization）的开源工具，内置 Whisper、PyAnnote 等模型，支持多语言处理，可通过 GPU 加速提升性能。

**使用方法**  
1. **部署方式**：  
   - 标准部署：使用 Docker 容器（支持 CPU 或 NVIDIA GPU）。  
   - GPU 部署：需安装 NVIDIA 驱动，使用专用 CUDA 镜像。  
   - Homebrew 安装：适用于 macOS 用户。  
2. **配置**：首次启动需初始化环境、下载模型并配置数据库，后续运行速度更快。  

**主要特性**  
- 支持多种语音模型（Whisper、NVIDIA NeMo 等）和说话人识别。  
- 提供 CPU/GPU 双模式部署，GPU 版本支持 CUDA 加速。  
- 隐私保护：本地处理数据，无云端传输。  
- 跨平台兼容：支持 Linux、macOS 及 NVIDIA GPU 环境。  
- 配置灵活：可通过环境变量调整安全策略（如 HTTPS 强制）。