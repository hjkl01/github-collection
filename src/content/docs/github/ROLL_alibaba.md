
---
title: ROLL
---

### [alibaba ROLL](https://github.com/alibaba/ROLL)  ![GitHub Repo stars](https://img.shields.io/github/stars/alibaba/ROLL?style=social)

ROLL 是一个面向大语言模型 (LLM) 的高效且用户友好的大规模强化学习 (RL) 扩展库。该项目基于 Ray 的多角色分布式架构，集成 Megatron-Core、SGLang 和 vLLM 等技术以加速模型训练与推理，旨在显著提升 LLM 在人类偏好对齐、复杂推理及多轮智能体交互场景下的性能。其核心功能涵盖支持 RLVR 及 Agentic 等多种训练流水线，提供包括 PPO、GRPO、Reinforce++ 在内的二十多种强化学习算法策略，支持分布式异步并行 rollout 与训练，兼容 NVIDIA、Ascend 及 AMD 等多种硬件，并具备设备映射优化、LoRA 微调支持及丰富的可观测性监控工具。