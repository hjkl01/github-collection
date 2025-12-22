
---
title: VoxCPM
---

### [OpenBMB VoxCPM](https://github.com/OpenBMB/VoxCPM)  ![GitHub Repo stars](https://img.shields.io/github/stars/OpenBMB/VoxCPM?style=social)

**项目核心内容总结：**

**功能**  
VoxCPM 是一个无需分词的文本到语音（TTS）模型，支持上下文感知的语音生成和高真实感的语音克隆，可进行个性化微调。

**使用方法**  
1. **命令行工具**：支持语音克隆、批量处理、参数调整（如音质/速度控制）、本地或Hugging Face模型加载。  
2. **Web界面**：通过 `python app.py` 启动UI，实现语音克隆与生成。  
3. **微调**：支持全量微调（SFT）和LoRA微调，适配个性化数据训练。

**主要特性**  
- 采样率高达44.1kHz，音质清晰。  
- 支持中英文，其他语言性能未保证。  
- 社区扩展：ComfyUI插件、ONNX导出、Apple Neural Engine后端等。  
- 风险控制：明确禁止非法用途，要求AI生成内容标注。

**限制与风险**  
- 语音克隆可能被用于伪造，需遵守法律伦理。  
- 长文本或复杂指令可能不稳定，控制力有限（如情感/语调调节不直接支持）。  
- 仅限研究开发，商用需测试验证。