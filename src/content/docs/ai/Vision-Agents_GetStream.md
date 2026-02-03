
---
title: Vision-Agents
---

### [GetStream Vision-Agents](https://github.com/GetStream/Vision-Agents)  ![GitHub Repo stars](https://img.shields.io/github/stars/GetStream/Vision-Agents?style=social)

### 项目核心内容总结

**项目名称：** Open Vision Agents by Stream

**项目功能：**  
Open Vision Agents 是一个用于构建实时视频 AI 代理的框架，结合视觉、语音、文本处理能力，支持多种 AI 模型（如 YOLO、Gemini、OpenAI、Claude 等）进行实时分析和交互。其目标是帮助开发者快速构建低延迟、多模态的视频 AI 应用，适用于体育指导、安防监控、虚拟助手、电话客服等场景。

**使用方法：**  
1. 安装：`uv add vision-agents`  
2. 可选安装额外插件：`uv add "vision-agents[getstream, openai, elevenlabs, deepgram]"`  
3. 使用 Stream API 密钥（可免费获取）进行初始化  
4. 定义 Agent，指定 LLM、语音处理、视频处理器等组件，如 YOLO、Gemini Realtime 等  

**主要特性：**  
- **实时视频 AI：** 支持视频、音频、文本的实时处理和分析。  
- **低延迟：** 通过 Stream 的边缘网络实现音频/视频延迟低于 30ms，连接速度 500ms 内。  
- **开放性：** 支持任意视频边缘网络，非仅限 Stream。  
- **原生 SDK：** 支持 OpenAI、Gemini、Claude 等主流 LLM 的原生接口。  
- **SDK 支持：** React、Android、iOS、Flutter、React Native、Unity 等多平台。  
- **插件生态：** 提供丰富插件，如 TTS（ElevenLabs、Cartesia）、STT（Deepgram、Wizper）、LLM（Gemini、OpenAI、xAI）、视频处理（YOLO、Roboflow）等。  
- **多模态处理：** 支持语音识别（STT）、语音合成（TTS）、目标检测、姿态识别、人脸识别、RAG（TurboPuffer）、电话集成（Twilio）等。  
- **示例丰富：** 提供多个完整示例，如高尔夫教练、安防监控、实时翻译、虚拟助手等。  
- **部署便捷：** 提供 HTTP API 和 Docker 部署方式，支持 GPU 加速。  

**适用场景：**  
- 体育指导（如高尔夫姿势分析）  
- 安防监控（如包裹丢失检测、自动发布通缉令）  
- 虚拟助手（如面试辅导、销售指导）  
- 电话客服（结合 RAG 技术提供专业知识）  
- 实时视频生成（如 Decart 风格化视频）  
- 语音交互（如 Cluely 风格的隐形助手）  

**开发语言：** Python  

**文档和教程：** 提供详细的入门指南、教程和示例代码，支持开发者快速上手。  

**未来规划：**  
- 增强插件生态，如 AWS、Qwen、NVIDIA、HuggingFace 等  
- 优化实时性能和稳定性  
- 提供部署工具和观测系统  
- 丰富示例和文档  

**限制：**  
- 视频 AI 对小文本识别较差  
- 长视频易丢失上下文  
- 实时模型对视频响应不直接，需结合音频/文本触发  

**招聘：** 招聘 Python 工程师，参与视频与语音 AI 工具开发。