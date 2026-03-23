### [OpenBMB MiniCPM-o](https://github.com/OpenBMB/MiniCPM-o)  ![GitHub Repo stars](https://img.shields.io/github/stars/OpenBMB/MiniCPM-o?style=social)

MiniCPM 系列是面向端侧部署的多模态大语言模型（MLLM），核心版本包括 MiniCPM-o 4.5 和 MiniCPM-V 4.0。

1. **多模态交互**：支持图像、视频、文本、音频输入及文本、语音输出。MiniCPM-o 4.5 具备全双工多模态实时流式对话能力，能同时“看、听、说”，支持语音克隆及主动交互，视觉与语音性能接近 Gemini 2.5 Flash；MiniCPM-V 4.0 专注于高效图像理解，支持 OCR、多图及视频分析。
2. **高效端侧部署**：支持多种量化格式（GGUF、int4、AWQ 等）及推理框架（llama.cpp-omni、vLLM、Ollama 等），可在手机（iOS）、Mac、PC 及 GPU 设备上低资源运行。
3. **完整生态**：提供 Web 演示（WebRTC）、Cookbook 使用手册及微调工具（LLaMA-Factory、SWIFT 等），支持跨芯片平台（FlagOS）部署。