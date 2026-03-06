
---
title: BitNet
---

### [microsoft BitNet](https://github.com/microsoft/BitNet)  ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/BitNet?style=social)

bitnet.cpp 是 1-bit 大语言模型（如 BitNet b1.58）的官方推理框架，基于 llama.cpp 构建。项目提供优化的计算内核，支持在 CPU 和 GPU 上实现快速且无损的模型推理。主要功能包括：支持 I2_S、TL1、TL2 等量化类型，兼容 BitNet、Llama3-8B、Falcon 等多种模型；在 ARM 和 x86 架构上相比常规实现可提升 1.37 至 6.17 倍的推理速度，能耗降低 55% 至 82%；具备在单台 CPU 上运行百 B 参数模型的能力，生成速度达人类阅读水平。