### [huggingface candle](https://github.com/huggingface/candle)  ![GitHub Repo stars](https://img.shields.io/github/stars/huggingface/candle?style=social)

Candle 是一个基于 Rust 的轻量级机器学习框架，专注于高性能（包括 GPU 支持）和易用性。其主要功能如下：

1. **简洁语法**：操作风格类似 PyTorch，支持模型训练及嵌入自定义算子（如 Flash Attention）。
2. **多后端支持**：提供优化的 CPU 后端（支持 MKL/Accelerate）、CUDA GPU 后端（支持多卡 NCCL）及 WASM 支持（可在浏览器运行）。
3. **丰富的模型覆盖**：内置大量主流模型示例，包括大语言模型（LLaMA、Mistral、Gemma、Phi 等）、文生图（Stable Diffusion）、语音识别（Whisper）、计算机视觉（YOLO、SAM、DINOv2）等。
4. **文件格式兼容**：支持加载 safetensors、ggml、PyTorch 及 npz 格式模型，并支持量化部署。
5. **核心目标**：旨在实现无服务器推理，去除生产环境中的 Python 依赖，便于 Rust 生态集成与轻量级部署。