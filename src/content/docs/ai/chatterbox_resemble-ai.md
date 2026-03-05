
---
title: chatterbox
---

### [resemble-ai chatterbox](https://github.com/resemble-ai/chatterbox)  ![GitHub Repo stars](https://img.shields.io/github/stars/resemble-ai/chatterbox?style=social)

Chatterbox TTS 是由 Resemble AI 开发的开源文本转语音（TTS）项目，主要功能如下：

1.  **多模型体系**：提供 Chatterbox-Turbo（350M 参数，低延迟，仅英语）、Chatterbox-Multilingual（500M 参数，支持 23+ 语言）和标准版 Chatterbox。
2.  **零样本语音克隆**：仅需 10 秒参考音频即可克隆目标音色，支持通过参考文件定制说话人声音。
3.  **高效推理**：Turbo 模型将解码步骤从 10 步优化至 1 步，大幅降低计算资源和显存占用，适合实时应用。
4.  **丰富表现力控制**：原生支持副语言标签（如 `[laugh]`、`[cough]`），并可调节 CFG 权重和夸张程度以控制语速和语气。
5.  **负责任 AI 保障**：内置 Perth 感知阈值水印，所有生成的音频均带有不可见的版权或来源标识。
6.  **易集成使用**：支持 Python 库直接安装和调用，提供示例代码，适用于语音助手、播客制作及交互媒体等场景。