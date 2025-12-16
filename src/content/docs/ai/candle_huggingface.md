
---
title: candle
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/huggingface/candle?style=social) ](https://github.com/huggingface/candle)
### [huggingface candle](https://github.com/huggingface/candle)

**项目核心内容总结：**

**1. 项目简介**  
Candle 是一个基于 Rust 的轻量级机器学习框架，旨在实现无服务器推理（Serverless Inference），支持多种后端（如 CUDA、MKL、Accelerate）和 ONNX 模型加载，适合部署轻量化机器学习服务。

**2. 主要功能**  
- 提供核心张量操作、设备管理及神经网络工具（如线性层、Transformer 模块）  
- 支持加载 Hugging Face 模型（如 LLaMA、BERT）和 ONNX 模型  
- 包含 CUDA 自定义内核（如 Flash Attention v2）优化计算性能  
- 提供数据集工具、模型训练示例及与 Hugging Face 生态集成（如 tokenizers、safetensors）  

**3. 使用方法**  
- 通过 Cargo 编译项目，运行示例（如 LLaMA 推理）  
- 加载模型需指定设备（CPU/GPU）及模型路径，支持多后端切换  
- 示例代码包含张量操作、模型训练及推理流程  

**4. 核心特性**  
- **轻量化**：无需依赖 Python，避免 GIL 限制，适合生产环境  
- **多后端支持**：兼容 CUDA、MKL、Accelerate 等加速库  
- **跨平台**：支持 Windows、Linux、WSL 等环境，提供常见错误解决方案（如 MKL 缺失符号、LLaMA 访问权限）  
- **高效推理**：通过 Flash Attention 等优化技术提升计算效率  

**5. 常见问题**  
- **模型加载失败**：需在 Hugging Face 注册并获取 LLaMA 模型授权  
- **编译错误**：需安装 MKL/Accelerate 库或调整 CUDA 编译器版本（如 gcc-10）  
- **Windows 链接错误**：需手动指定 native 库路径或重命名 CUDA 相关 DLL 文件