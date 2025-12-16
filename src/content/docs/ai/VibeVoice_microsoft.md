
---
title: VibeVoice
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/VibeVoice?style=social) ](https://github.com/microsoft/VibeVoice)
### [microsoft VibeVoice](https://github.com/microsoft/VibeVoice)

**项目核心内容总结：**

VibeVoice 是微软开源的语音生成框架，支持从文本生成**多说话人、长篇幅**（最长90分钟）的自然对话音频（如播客），并提供**实时流式TTS**模型（首句延迟约300ms）。其核心创新包括：  
- 使用7.5Hz超低帧率的**连续语音分词器**（语义与声学），兼顾音质与计算效率；  
- 基于**LLM+扩散框架**，理解上下文并生成高保真语音。  

**使用方法**：  
- 通过 Colab 示例（[链接](https://colab.research.google.com/github/microsoft/VibeVoice/blob/main/demo/vibevoice_realtime_colab.ipynb)）体验实时TTS；  
- 通过 WebSocket 示例启动本地演示（见文档 [Usage](docs/vibevoice-realtime-0.5b.md)）；  
- 从 Hugging Face 获取模型集合（[链接](https://huggingface.co/collections/microsoft/vibevoice-68a2ef24a875c44be47b034f)）。  

**主要限制与风险**：  
- 仅支持**中英文**，其他语言可能生成异常音频；  
- **不处理背景音、音乐或重叠语音**；  
- 高质量合成语音可能被用于**深度伪造或虚假信息**，需确保文本可靠性并合法使用；  
- 项目曾因滥用风险暂停，当前仅限**研究用途**，不推荐直接用于商业场景。