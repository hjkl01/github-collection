
---
title: index-tts
---

### [index-tts index-tts](https://github.com/index-tts/index-tts)  ![GitHub Repo stars](https://img.shields.io/github/stars/index-tts/index-tts?style=social)

IndexTTS2 是一款零样本自回归文本转语音（TTS）模型，具备高度情感表达和时长控制能力，核心功能如下：

1. **时长精确控制**：支持指定生成 Token 数量以精确控制语音时长，或自由生成并保留输入韵律特征。
2. **音色与情感解耦**：独立控制音色（来自参考音频）和情感（来自风格提示或文本），实现零样本语音克隆。
3. **多模态情感调控**：支持通过情感参考音频、自然语言文本描述（经 Qwen3 微调）或情感向量灵活调节情感强度。
4. **高保真合成**：采用三阶段训练和 GPT 隐式表示，提升高情感表达下的清晰度与稳定性，支持中英文，各项指标达 SOTA 水平。
5. **便捷使用**：提供 WebUI 界面及 Python 脚本接口，支持 FP16 及 DeepSpeed 加速。