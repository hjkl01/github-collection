
---
title: ComfyUI
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/comfyanonymous/ComfyUI?style=social) ](https://github.com/comfyanonymous/ComfyUI)
### [comfyanonymous ComfyUI](https://github.com/comfyanonymous/ComfyUI)

**核心内容总结：**

ComfyUI 是一个基于节点的图形界面工具，用于生成和管理 AI 图像生成流程。其主要功能包括：

- **项目功能**：通过节点连接的方式构建图像生成流程，支持自定义节点的安装和管理（通过 ComfyUI-Manager）。
- **使用方法**：运行 `python main.py` 启动工具，支持命令行参数（如启用管理器、设置 TLS/SSL、启用高质量预览等）。
- **主要特性**：
  - 支持多种 GPU（包括 AMD、NVIDIA、Intel 等）；
  - 提供高质量图像预览（通过 TAESD 模型）；
  - 支持动态提示词、文本嵌入（Textual Inversion）、种子保存等功能；
  - 支持 TLS/SSL 加密连接；
  - 提供前端管理界面（通过 ComfyUI-Manager）用于安装和更新自定义节点；
  - 支持多种硬件加速（如 ROCm、CUDA）和实验性功能（如内存高效注意力机制）。

ComfyUI 适用于 AI 图像生成领域的开发者和艺术家，提供灵活、高效的图像生成工作流程管理。