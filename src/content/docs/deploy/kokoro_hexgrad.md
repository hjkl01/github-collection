
---
title: kokoro
---

### [hexgrad kokoro](https://github.com/hexgrad/kokoro)  ![GitHub Repo stars](https://img.shields.io/github/stars/hexgrad/kokoro?style=social)

kokoro 是一个用于 Kokoro-82M 文本转语音（TTS）模型的推理库。该模型为 8200 万参数的开源轻量级模型，采用 Apache 许可证，具备高音质、低延迟和高成本效益。库提供 `KPipeline` Python API，支持美式/英式英语、中文、日语、西班牙语、法语、印地语、意大利语及葡萄牙语等多种语言。功能包括自定义语音音色、语速调节、文本分段，支持音频实时播放与 WAV 文件保存。底层集成 Misaki G2P 库处理文本，兼容 Linux、Windows 及 macOS 平台（支持 Apple Silicon GPU 加速），需配置 espeak-ng 环境，适用于生产环境及个人项目部署。