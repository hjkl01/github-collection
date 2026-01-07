
---
title: faster-whisper
---

### [SYSTRAN faster-whisper](https://github.com/SYSTRAN/faster-whisper)  ![GitHub Repo stars](https://img.shields.io/github/stars/SYSTRAN/faster-whisper?style=social)

**项目核心内容总结：**  
该项目是一个基于CTranslate2的高效语音识别工具库（**faster-whisper**），兼容Hugging Face的Whisper模型，支持多种功能：  
1. **核心功能**：  
   - 高性能语音转文字，支持原生Whisper模型及Distil-Whisper轻量版本；  
   - 提供词级时间戳、VAD静音过滤、批量处理等高级功能；  
   - 支持模型量化（如FP16）以提升推理速度。  

2. **使用方法**：  
   - 安装依赖后，通过`WhisperModel`加载预训练模型（如`"large-v3"`或`"distil-large-v3"`）；  
   - 调用`transcribe`方法，可指定参数（如语言、beam size、VAD过滤等）；  
   - 支持批量处理（通过`BatchedInferencePipeline`）及模型自定义转换（从Hugging Face导入或本地加载）。  

3. **主要特性**：  
   - **高效性**：相比原生Whisper，推理速度显著提升；  
   - **灵活性**：支持多种模型、量化格式及参数定制；  
   - **集成能力**：内置Silero VAD静音检测，兼容社区工具（如WhisperX、Open-Dubbing等）；  
   - **易用性**：提供CLI工具、API接口及跨平台部署方案（Windows/Linux/macOS）。  

**模型转换**：支持从Hugging Face下载或本地转换模型，通过`ct2-transformers-converter`工具生成CTranslate2格式模型。