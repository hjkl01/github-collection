
---
title: ROLL
---

### [alibaba ROLL](https://github.com/alibaba/ROLL)

ROLL是一个由阿里巴巴开发的强化学习优化库，专注于大规模机器学习任务。其核心功能包括：  
1. **多任务训练（RLVR）**：支持数学、编程、开放问答等场景，提供异步并行执行、动态采样和灵活的任务分布控制。  
2. **多轮交互训练（Agentic RL）**：适用于游戏、对话等场景，支持环境级异步并行、多轮交互调试及两种训练范式（TrajectoryWise和StepWise）。  
3. **算法与引擎支持**：内置20+强化学习策略（如PPO、GRPO），兼容多种训练框架（DeepSpeed、Megatron-LM）和推理引擎（vLLM、SGLang），支持LoRA、FP8等技术。  
4. **自动化与可观测性**：自动设备映射管理、集成SwanLab/WandB/TensorBoard性能追踪，支持大规模分布式训练（单机至千GPU集群）。  

**使用方法**：通过配置策略和后端引擎，可灵活部署训练或推理任务，适用于LLM/VLM的预训练、微调及蒸馏等场景。