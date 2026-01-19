
---
title: neutts
---

### [neuphonic neutts](https://github.com/neuphonic/neutts)  ![GitHub Repo stars](https://img.shields.io/github/stars/neuphonic/neutts?style=social)

### 项目核心内容总结

**项目功能**  
NeuTTS 是一套开源的语音合成（TTS）模型，支持本地设备部署，具备实时语音克隆能力。通过结合轻量级语言模型和高效音频编码器（NeuCodec），可生成自然语音，并支持多设备运行（手机、嵌入式设备等）。

**主要特性**  
- 支持英语语音合成，提供两种模型（NeuTTS-Air 和 NeuTTS-Nano），参数量分别为 ~360M 和 ~120M，支持语音克隆功能。  
- 使用 GGML 格式优化本地推理，兼容 GGUF 量化版本（Q4/Q8），可在 CPU 或 GPU 上运行。  
- 集成水印技术，确保生成音频的可追溯性。  
- 推理速度：在中端设备上实现实时生成，RTX 4090 显卡下可达 1.9 万 tokens/s（Nano 模型）。  

**使用方法**  
1. **安装依赖**：克隆仓库，安装 `espeak-ng`（语音相关依赖），Python 依赖（PyTorch、llama-cpp-python、onnxruntime 等）。  
2. **运行示例**：通过命令行或 Python 脚本调用模型，需提供输入文本、参考音频及文本（用于语音克隆）。  
3. **流式生成**：支持分块生成音频，需安装 `pyaudio`。  
4. **模型选择**：可指定不同模型版本（如 `neutts-nano-q4-gguf`）及编码器（NeuCodec）。  

**注意事项**  
- 项目由 Neuphonic 官方维护，警惕非官方网站（如 neutts.com）。  
- 生成音频包含水印，避免用于非法用途。  
- Python 环境需 3.11-3.13 版本，依赖 PyTorch 兼容性。