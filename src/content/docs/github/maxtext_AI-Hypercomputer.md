
---
title: maxtext
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/AI-Hypercomputer/maxtext?style=social) ](https://github.com/AI-Hypercomputer/maxtext)
### [AI-Hypercomputer maxtext](https://github.com/AI-Hypercomputer/maxtext)

**MaxText 核心内容总结：**

**项目功能**  
MaxText 是一个高性能、可扩展的开源大语言模型（LLM）库，基于 Python/JAX，专为 Google Cloud TPU/GPU 优化。支持多种模型（如 Gemma、Llama、Qwen、Mistral 等）的预训练（支持数万芯片规模）和微调（SFT、GRPO/RL 等技术），并提供多模态训练能力（如 Gemma 3、Llama 4 VLM）。

**使用方法**  
- 安装：通过 PyPI（`pip install maxtext`）或阅读文档指南安装。  
- 运行：支持单机/多机 TPU/GPU 训练，提供单机和多机微调教程（SFT/RL）。  
- 解耦模式：无需依赖 GCP 即可运行。  

**主要特性**  
1. **高性能**：利用 JAX/XLA 实现高 MFU（模型 FLOPs 利用率）和高吞吐（token/s），优化无冗余。  
2. **模型支持**：覆盖主流开源模型（如 Llama 4、Qwen 3 MoE、DeepSeek-V3 等），支持稠密模型与 MoE（专家混合）模型。  
3. **扩展性**：支持大规模集群训练，提供词汇分片（Vocabulary Tiling）、多令牌预测（MTP）等优化技术。  
4. **工具链集成**：整合 Flax（神经网络）、Tunix（微调）、Orbax（检查点）、Optax（优化）等库，支持全流程训练与推理。  

**其他**  
- 提供模型库、性能指标文档、教程（如首次运行、SFT/RL 指南）。  
- 社区支持：通过 Discord 参与，GitHub 提交反馈。