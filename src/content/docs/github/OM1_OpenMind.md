
---
title: OM1
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/OpenMind/OM1?style=social) ](https://github.com/OpenMind/OM1)
### [OpenMind OM1](https://github.com/OpenMind/OM1)

**核心内容总结：**  
OM1 是 OpenMind 推出的模块化 AI 运行时系统，支持开发者创建和部署多模态 AI 代理到数字环境及物理机器人（如人形机器人、四足机器人、教育机器人等）。代理可处理摄像头、激光雷达、社交媒体等多源数据，并执行运动、导航、对话等物理动作。  

**主要特性：**  
- **模块化架构**：基于 Python 开发，支持灵活扩展。  
- **硬件兼容性**：通过插件支持 ROS2、Zenoh、CycloneDDS 等接口，推荐使用 Zenoh。  
- **调试工具**：提供 WebSim（http://localhost:8000/）实时监控系统状态。  
- **预配置服务**：集成 TTS、多 LLM（OpenAI、Anthropic 等）及视觉语言模型（VLM）的 API 端点。  

**使用方法：**  
1. 安装 `uv` 包管理器，克隆仓库并初始化子模块。  
2. 根据系统（MacOS/Linux）安装依赖（如 portaudio、ffmpeg）。  
3. 从 OpenMind 门户获取 API 密钥，配置到 `spot.json5` 或 `.env` 文件。  
4. 运行示例代理（如 `uv run src/run.py spot`），通过 WebSim 查看调试信息。  
5. 高级用户可通过 Docker 启动全自主模式（集成 `om1`、`unitree_sdk`、`om1-avatar`、`om1-video-processor` 服务）。  

**推荐开发平台：**  
Jetson AGX Orin、Mac Studio/M4 Pro、Ubuntu 22.04 等。