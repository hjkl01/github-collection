
---
title: ROLL
---

### [alibaba ROLL](https://github.com/alibaba/ROLL)  ![GitHub Repo stars](https://img.shields.io/github/stars/alibaba/ROLL?style=social)

ROLL 是一款面向大语言模型（LLM）的高效强化学习优化库，旨在利用大规模 GPU 资源提升模型在人类偏好对齐、复杂推理及多轮智能体交互中的性能。该项目基于 Ray 构建多角色分布式架构，集成 Megatron-Core、SGLang 和 vLLM 以加速模型训练与推理。核心功能涵盖 RLVR、智能体强化学习、蒸馏、DPO 及 SFT 等多种训练管道，内置 PPO、GRPO 等二十余种强化学习算法。项目兼容 NVIDIA、AMD 及 Ascend 硬件，支持 Qwen 系列及视觉语言模型（VLM），并提供异步并行 rollout、LoRA 微调、FP8 推理及多平台观测追踪等高级特性。