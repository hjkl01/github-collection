
---
title: GPT-SoVITS
---

### [RVC-Boss GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)

**项目核心内容总结：**

**功能**  
GPT-SoVITS 是一个支持语音合成（TTS）、语音克隆、音色转换及音频处理的工具，可生成高质量人声、实现多音色转换，并集成 UVR5 音频分离功能。

**使用方法**  
1. **WebUI 操作**：通过图形界面完成模型训练、语音合成、音色转换及音频处理（如 UVR5 音频分离）。  
2. **命令行工具**：支持音频切分、ASR 识别、模型推理等任务，例如使用 `audio_slicer.py` 切分音频，`fasterwhisper_asr.py` 进行非中文 ASR 识别。  
3. **Docker 部署**：提供容器化部署方案，简化环境配置。  

**主要特性**  
- **多语言支持**：涵盖中文、日语、英语，支持粤语训练数据。  
- **模型版本**：提供多个优化版本（v2Pro、v3、v4 等），v4 支持原生 48k 音频输出，v2Pro 在性能上优于 v2。  
- **高音质合成**：基于 SoVITS 和 GPT 架构，结合 BigVGAN 等 vocoder 提升音频质量。  
- **集成工具**：整合 UVR5（音频分离）、audio-slicer（音频切分）、FunASR（ASR 识别）等第三方工具。  
- **扩展性**：支持自定义训练数据、模型混合及不同规模模型（如轻量级模型开发计划）。  

**依赖**  
依赖 PyTorch、FFmpeg、Gradio 等库，部分功能需 NVIDIA GPU 及 CUDA 支持。