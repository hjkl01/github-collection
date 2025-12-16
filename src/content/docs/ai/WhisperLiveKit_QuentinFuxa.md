
---
title: WhisperLiveKit
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/QuentinFuxa/WhisperLiveKit?style=social) ](https://github.com/QuentinFuxa/WhisperLiveKit)
### [QuentinFuxa WhisperLiveKit](https://github.com/QuentinFuxa/WhisperLiveKit)

WhisperLiveKit 是一个支持实时语音转文字（STT）及说话人识别的工具，具有以下核心功能和特性：  
- **功能**：提供超低延迟的语音识别，支持多语言翻译（NLLB）、说话人识别（Diarization）及 LoRA 模型微调，适用于会议记录、无障碍辅助、媒体内容生成等场景。  
- **使用方法**：通过命令行参数配置后端策略（如 SimulStreaming 或 LocalAgreement）、语音活动检测（VAD）、SSL 证书、翻译选项等，支持 Docker 部署（含 GPU/CPU 优化）和 Nginx 生产环境配置。  
- **特性**：兼容多种后端（Faster-Whisper、MLX-Whisper、原生 Whisper），支持自定义音频缓冲参数（如帧阈值、最大上下文长度），提供 Docker 镜像加速部署，允许通过 Hugging Face 登录下载受限制模型。