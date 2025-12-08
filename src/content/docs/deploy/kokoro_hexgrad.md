
---
title: kokoro
---

### [hexgrad kokoro](https://github.com/hexgrad/kokoro)

**项目功能**  
Kokoro 是一个基于 8200 万参数的开放权重文本到语音（TTS）模型的推理库，支持多语言（如英语、西班牙语、法语、日语、中文等），提供高质量语音合成，且模型轻量、运行速度快、成本低。权重采用 Apache 许可证，可自由部署于生产环境或个人项目。

**使用方法**  
1. 安装依赖：通过 `pip install kokoro` 安装库，Windows 需额外安装 espeak-ng。  
2. 初始化管道：使用 `KPipeline` 指定语言代码（如 `'a'` 表示美式英语），输入文本并选择语音风格（如 `'af_heart'`）。  
3. 生成音频：通过 `pipeline(text, voice=..., speed=...)` 生成语音，支持分段输出、保存为 WAV 文件及实时播放。  

**主要特性**  
- 支持多语言（需安装对应语言包）；  
- 轻量级模型，性能接近大模型但更高效；  
- 提供高级配置（如语音风格、速度、分段规则）；  
- 支持 Windows、MacOS（含 Apple Silicon GPU 加速）及 Conda 环境部署。