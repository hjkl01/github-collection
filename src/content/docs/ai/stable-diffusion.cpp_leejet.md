
---
title: stable-diffusion.cpp
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/leejet/stable-diffusion.cpp?style=social) ](https://github.com/leejet/stable-diffusion.cpp)
### [leejet stable-diffusion.cpp](https://github.com/leejet/stable-diffusion.cpp)

**项目核心内容总结：**

**项目功能**  
`stable-diffusion.cpp` 是一个基于纯 C/C++ 实现的扩散模型推理框架，支持多种图像生成模型（如 Stable Diffusion、Flux、Wan 等）、图像编辑模型和视频模型，兼容 CPU/GPU 多平台运行，无外部依赖。

**使用方法**  
1. 下载预编译的二进制文件或从源码构建项目；  
2. 从 HuggingFace 等平台获取模型权重文件；  
3. 通过命令行工具（如 `./bin/sd -m [模型路径] -p [提示词]`）生成图像。

**主要特性**  
- **模型支持**：涵盖 SD 系列（SD1.x/2.x/XL/3）、Flux、Chroma、Qwen Image、Wan2.1/2.2 等主流模型，支持 PhotoMaker、ControlNet、LoRA、LCM 等扩展功能；  
- **多平台兼容**：支持 Linux、Mac、Windows、Android（通过 Termux/Local Diffusion）；  
- **性能优化**：提供 Flash Attention、VAE 分块处理、多种采样算法（Euler A、DPM++ 2M 等）、负提示、参数嵌入 PNG 输出等；  
- **跨平台可重复性**：通过 `--rng` 参数适配不同平台的随机数生成；  
- **开发友好**：提供 Python、Rust、C#、Go 等语言的绑定接口，支持多种 UI 工具（如 Jellybox、Stable Diffusion GUI）。