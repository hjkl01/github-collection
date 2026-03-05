
---
title: maxtext
---

### [AI-Hypercomputer maxtext](https://github.com/AI-Hypercomputer/maxtext)  ![GitHub Repo stars](https://img.shields.io/github/stars/AI-Hypercomputer/maxtext?style=social)

MaxText 是一个基于纯 Python 和 JAX 编写的高性能、高可扩展性开源大语言模型（LLM）库及参考实现，主要针对 Google Cloud TPUs 和 GPU 进行训练优化。

核心功能包括：
1. **广泛模型支持**：内置并优化了 Gemma、Llama、DeepSeek、Qwen、Mistral 等主流模型，支持多模态训练。
2. **全流程训练**：支持从单主机到超大规模集群的预训练及后训练（含 SFT、RL 等强化学习技术）。
3. **高性能与易用性**：利用 JAX 和 XLA 实现高模型浮点运算利用率（MFU）和高吞吐量，架构简洁无需手动优化。
4. **生态整合**：集成 Flax、Tunix、Orbax、Optax、Grain 等库，支持分片、量化、检查点及词汇平铺等高级功能。
5. **灵活部署**：提供 PyPI 包安装，支持无 GCP 依赖的去耦模式运行。