
---
title: whisper
---

### [openai whisper](https://github.com/openai/whisper)

**Whisper** 是 OpenAI 开发的通用语音识别模型，支持多语言语音识别、语音翻译和语言识别。模型基于 Transformer 架构，通过多任务训练实现多种语音处理功能。提供多种模型版本（如 tiny、base、small、medium、large、turbo），适用于不同硬件和性能需求，其中 turbo 模型优化了转录速度，但仅适用于英文；其他模型支持多语言翻译。安装需 Python、PyTorch、tiktoken 和 ffmpeg，部分情况下需 Rust 环境。可通过命令行或 Python API 进行音频转录，翻译任务需使用多语言模型（如 medium、large）。许可证为 MIT。