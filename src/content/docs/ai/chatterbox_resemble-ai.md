
---
title: chatterbox
---

### [resemble-ai chatterbox](https://github.com/resemble-ai/chatterbox)  ![GitHub Repo stars](https://img.shields.io/github/stars/resemble-ai/chatterbox?style=social)

**项目核心内容总结：**  
Chatterbox TTS 是 Resemble AI 开发的开源文本转语音（TTS）模型家族，包含三个版本，其中 **Chatterbox-Turbo** 是最高效的模型，参数量为 350M，支持英文及多种语言（23+种），具备以下特性：  
1. **高效性**：计算资源和显存需求低于以往模型，生成速度更快（解码步骤从 10 步减少至 1 步）。  
2. **拟声功能**：支持通过 `[cough]`、`[laugh]` 等标签添加拟声效果，提升语音真实感。  
3. **多语言支持**：覆盖英语、中文、法语、西班牙语等 23 种语言。  
4. **内置水印**：生成的音频包含不可感知的神经水印，可抵御压缩和编辑。  

**使用方法**：  
- 安装：`pip install chatterbox-tts` 或从源码安装。  
- 生成语音：通过 Python 调用模型（如 `ChatterboxTurboTTS.generate()`），需提供文本和参考音频（用于语音克隆）。  

**适用场景**：  
- 低延迟语音助手、叙事创作、多语言应用等。