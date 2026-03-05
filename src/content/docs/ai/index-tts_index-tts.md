
---
title: index-tts
---

### [index-tts index-tts](https://github.com/index-tts/index-tts)  ![GitHub Repo stars](https://img.shields.io/github/stars/index-tts/index-tts?style=social)

IndexTTS2 是一款自回归零样本文本转语音（TTS）模型，核心功能总结如下：

1.  **时长可控**：首创支持精确指定生成时长（显式 Token 数）与自然自由生成模式相结合的时长适应方案，适用于视频配音等强同步场景。
2.  **情感解耦**：实现情感表达与说话人身份分离，支持通过音频提示、文本描述（基于微调 Qwen3）及向量灵活控制情感，且不影响音色还原。
3.  **语音克隆**：支持零样本音色重构，仅需少量参考音频即可准确复刻目标声纹。
4.  **高性能**：在字错率、说话人相似度和情感保真度上优于当前最先进的零样本 TTS 模型。
5.  **多语言与易用性**：支持中英文等多语言合成，提供 WebUI 及 Python API 接口，兼容 FP16、DeepSpeed 等推理加速选项。