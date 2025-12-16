
---
title: ktransformers
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/kvcache-ai/ktransformers?style=social) ](https://github.com/kvcache-ai/ktransformers)
### [kvcache-ai ktransformers](https://github.com/kvcache-ai/ktransformers)

**项目核心内容总结：**  
KTransformers 是一个基于 CPU-GPU 异构计算的高效大语言模型（LLM）推理与微调框架，包含两个核心模块：  

1. **kt-kernel（高性能推理内核）**  
   - **功能**：提供 CPU/GPU 优化的推理加速，支持混合专家（MoE）模型、量化（INT4/INT8）、多 GPU/多并发等。  
   - **特性**：  
     - 支持 Intel AMX/AVX 加速、AMD ROCm、Ascend NPU 等硬件。  
     - 支持 DeepSeek-V3/R1、Qwen3-Next、Kimi-K2 等主流模型。  
     - 可通过 Python API 集成至 SGLang 等框架。  
   - **使用方法**：  
     ```bash  
     cd kt-kernel  
     pip install .  
     ```  

2. **kt-sft（微调框架）**  
   - **功能**：与 LLaMA-Factory 集成，支持超大规模 MoE 模型（如 671B 参数 DeepSeek-V3）的高效微调。  
   - **特性**：  
     - 支持 LoRA 微调、异构加速（CPU/GPU 混合）。  
     - 资源占用低，70GB GPU 内存即可微调 671B 模型。  
   - **使用方法**：  
     ```bash  
     cd kt-sft  
     USE_KT=1 llamafactory-cli train examples/train_lora/deepseek3_lora_sft_kt.yaml  
     ```  

**主要优势**：  
- 推理性能：支持 24GB VRAM 下 8K 上下文、3~28 倍加速（如 DeepSeek-V3）。  
- 硬件兼容性：覆盖 Intel、AMD、Ascend 等多平台，支持 FP8、AMX、混合精度等技术。  
- 持续更新：集成 Kimi-K2、Qwen3-Next 等新模型，支持多 GPU、长上下文等场景。