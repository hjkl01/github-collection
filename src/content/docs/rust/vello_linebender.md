
---
title: vello
---

### [linebender vello](https://github.com/linebender/vello)  ![GitHub Repo stars](https://img.shields.io/github/stars/linebender/vello?style=social)

Vello 是基于 Rust 编写的以 GPU 计算为核心的 2D 图形渲染引擎。它利用 wgpu 调用 GPU，能够高效绘制大型 2D 场景，实现交互或近交互性能。引擎采用类似 PostScript 的 API，支持渲染形状、图像、渐变和文本等元素，常作为 GUI 工具（如 Xilem）的渲染后端。目前项目处于 Alpha 阶段，部分功能（如模糊效果、合并伪影处理）仍在完善中。支持 Web（依赖 WebGPU）及 Android 等跨平台，并提供 SVG、Lottie 等集成扩展。