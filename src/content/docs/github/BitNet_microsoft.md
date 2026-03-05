
---
title: BitNet
---

### [microsoft BitNet](https://github.com/microsoft/BitNet)  ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/BitNet?style=social)

bitnet.cpp 是微软官方推出的 1-bit 大语言模型（如 BitNet b1.58）推理框架。它提供优化内核，支持在 CPU 和 GPU 上进行快速、无损的推理，显著提升了 ARM 和 x86 平台的运行速度（最高 6.17 倍）并降低能耗（最高 82.2%），支持单 CPU 运行百亿参数模型。项目基于 llama.cpp 构建，支持多种 1-bit 量化格式（I2_S, TL1, TL2）及多个主流模型（如 BitNet、Llama3、Falcon），提供源码编译、模型转换及推理测试工具。