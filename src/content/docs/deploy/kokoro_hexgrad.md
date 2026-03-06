
---
title: kokoro
---

### [hexgrad kokoro](https://github.com/hexgrad/kokoro)  ![GitHub Repo stars](https://img.shields.io/github/stars/hexgrad/kokoro?style=social)

Kokoro 是一个用于 Kokoro-82M 开源文本转语音（TTS）模型的推理库。该模型拥有 8200 万参数，架构轻量，音质媲美大模型，同时速度快、成本低，采用 Apache 许可。项目通过 `pip` 安装，提供 `KPipeline` 接口，支持生成美式/英式英语、西班牙语、法语、印地语、意大利语、日语、巴西葡萄牙语及普通话中文等多种语音。底层基于 `misaki` 实现文本转音素（G2P），依赖 `espeak-ng` 进行音素转换。支持 Windows、macOS（含 Apple Silicon GPU 加速）及 Conda 环境，可完成音频的生成、播放及保存。