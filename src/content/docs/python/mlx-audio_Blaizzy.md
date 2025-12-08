
---
title: mlx-audio
---

### [Blaizzy mlx-audio](https://github.com/Blaizzy/mlx-audio)

**核心内容总结：**  
MLX-Audio 是基于 Apple MLX 框架开发的文本转语音（TTS）和语音转语音（STS）库，专为 Apple Silicon 优化，具备以下功能与特性：  
- **核心功能**：支持多语言语音合成、语音定制、速度调节（0.5x-2.0x）、实时 3D 音频可视化、REST API 接口、量化优化以提升性能，并可通过 Finder/Explorer 直接访问输出文件。  
- **使用方法**：通过 pip 安装后，可使用命令行或 Python API 调用（如 `generate_audio` 函数），并支持启动 FastAPI 服务器以访问网页界面；Swift 集成提供 iOS 开发接口，支持单次生成、流式生成及原始音频输出。  
- **主要特性**：高效推理、交互式 3D 可视化、多语言支持、灵活的语音参数定制、量化优化、跨平台（支持 Python 与 Swift）。