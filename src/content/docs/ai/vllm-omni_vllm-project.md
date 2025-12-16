
---
title: vllm-omni
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/vllm-project/vllm-omni?style=social) ](https://github.com/vllm-project/vllm-omni)
### [vllm-project vllm-omni](https://github.com/vllm-project/vllm-omni)

**项目核心内容总结：**  

**功能**：vLLM-Omni 是一个扩展自 vLLM 的框架，支持全模态（文本、图像、视频、音频）模型的推理与服务，适用于自回归（AR）和非自回归（如 Diffusion Transformers）架构，可输出多模态结果。  

**主要特性**：  
- **高效性能**：基于 vLLM 的高效 KV 缓存管理、流水线执行重叠、动态资源分配，提升吞吐量。  
- **灵活易用**：支持异构流水线抽象、Hugging Face 模型集成、分布式推理（张量/流水线/数据/专家并行）、流式输出、OpenAI 兼容 API。  
- **全模态支持**：兼容主流开源模型（如 Qwen-Omni、Qwen-Image）。  

**使用方法**：  
- 通过文档链接（[Read the Docs](https://vllm-omni.readthedocs.io/en/latest/)）获取安装指南、快速入门教程及支持模型列表。  

**许可证**：Apache License 2.0。