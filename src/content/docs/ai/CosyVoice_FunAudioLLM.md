
---
title: CosyVoice
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/FunAudioLLM/CosyVoice?style=social) ](https://github.com/FunAudioLLM/CosyVoice)
### [FunAudioLLM CosyVoice](https://github.com/FunAudioLLM/CosyVoice)

**项目核心内容总结：**  
CosyVoice 是一个支持多语言（中、英、日、粤语、韩语）的零样本文本到语音合成系统，具备跨语言合成、语音转换、流式语音生成等功能。CosyVoice 2 引入大语言模型实现流式合成，CosyVoice 3 通过扩展训练和后训练优化语音自然度。  

**使用方法：**  
1. **快速体验**：通过 Web 演示界面（`webui.py`）直接测试语音合成。  
2. **部署服务**：支持 Docker 部署，提供 gRPC 和 FastAPI 接口，适配不同推理模式（零样本、跨语言、指令控制等）。  
3. **加速部署**：使用 Nvidia TensorRT-LLM 加速推理，相比传统方案提升 4 倍效率。  

**主要特性：**  
- 支持零样本合成（无需预训练语音数据）；  
- 跨语言合成（支持中、英、日等语言切换）；  
- 语音转换（通过参考语音调整目标语音风格）；  
- 流式处理（实时生成语音）；  
- 可扩展部署（兼容 Docker、TensorRT-LLM）。