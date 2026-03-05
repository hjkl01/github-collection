
---
title: faster-whisper
---

### [SYSTRAN faster-whisper](https://github.com/SYSTRAN/faster-whisper)  ![GitHub Repo stars](https://img.shields.io/github/stars/SYSTRAN/faster-whisper?style=social)

faster-whisper 是基于 CTranslate2 引擎重新实现的 OpenAI Whisper 语音转录库。相比原版，它在保持相同准确性的情况下速度提升约 4 倍，内存占用更低，并支持 CPU 和 GPU 上的 8 位量化以进一步提升效率。

该库提供简洁的 Python API，具备以下核心功能：
- 支持批量转录、Distil-Whisper 模型及词级时间戳。
- 集成 VAD（语音活动检测）过滤器。
- 无需系统安装 FFmpeg，音频解码由 PyAV 库内置处理。
- 支持自动从 Hugging Face Hub 下载模型或转换自定义 Transformers 模型。

适用于对性能要求较高的语音转文本应用场景。