
---
title: OM1
---

### [OpenMind OM1](https://github.com/OpenMind/OM1)  ![GitHub Repo stars](https://img.shields.io/github/stars/OpenMind/OM1?style=social)

OpenMind OM1 是一个模块化 AI 运行时，旨在帮助开发者创建和部署多模态 AI 代理，支持数字环境（App、网站）及物理机器人（人形、四足、教育机器人等）。

核心功能包括：
1. **多模态交互**：支持网络、社交媒体、摄像头、激光雷达等多样输入，能执行运动、自主导航及自然对话等动作。
2. **插件化架构**：基于 Python 构建，通过插件接入新硬件与传感器，兼容 ROS2、Zenoh、CycloneDDS 等通信协议。
3. **开发支持**：提供 Web 可视化调试界面（WebSim），预配置了文本转语音（TTS）及多种大语言模型（LLM）和视觉语言模型（VLM）端点。
4. **硬件集成与自主运行**：通过硬件抽象层（HAL）连接机器人，支持 USB、串口、DDS 等接口；结合 BrainPack 组件提供 SLAM、视频处理、UI 及容器管理等全自主服务。