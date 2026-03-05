
---
title: ktransformers
---

### [kvcache-ai ktransformers](https://github.com/kvcache-ai/ktransformers)  ![GitHub Repo stars](https://img.shields.io/github/stars/kvcache-ai/ktransformers?style=social)

KTransformers 是一个基于 CPU-GPU 异构计算的大语言模型高效推理与微调框架。主要包含两个核心模块：

1. **kt-kernel**：高性能推理内核，支持 Intel AMX/AVX 加速、MoE 优化、多种量化（INT4/INT8/FP8/GPTQ）及 CPU-GPU 专家调度，可集成 SGLang 等框架。
2. **kt-sft**：微调框架，与 LLaMA-Factory 集成，支持超大规模 MoE 模型（如 671B）的低资源 LoRA 微调，大幅降低显存需求。

项目支持 DeepSeek、Kimi、Qwen 等主流模型，兼容 GPU、CPU、Ascend NPU 及 AMD GPU 等多种硬件，适用于低成本超大模型训推一体化场景。