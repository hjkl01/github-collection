
---
title: RLinf
---

### [RLinf RLinf](https://github.com/RLinf/RLinf)  ![GitHub Repo stars](https://img.shields.io/github/stars/RLinf/RLinf?style=social)

RLinf 是一个面向具身智能（Embodied AI）和 Agent AI 的灵活、可扩展开源强化学习基础设施。其核心功能包括：

1.  **灵活高效的训练框架**：支持 PPO、GRPO、SAC 等多种强化学习算法，隐藏分布式编程复杂性，支持大规模 GPU 节点扩展，兼容 FSDP、Megatron 等多后端以提升执行效率。
2.  **广泛的模型适配**：涵盖 VLA（如 π₀、GR00T、OpenVLA）、VLM（如 Qwen2.5-VL）及世界模型（如 OpenSora、Wan），支持强化学习微调、监督微调（SFT）及基于世界模型的 RL 训练。
3.  **多场景覆盖**：兼容 ManiSkill、IsaacLab、MetaWorld 等主流模拟器，支持 Franka 等真实机器人训练，以及 Agent 搜索、在线编码与推理任务，支持 Sim-Real 共训练。
4.  **易用性与部署**：支持通过 PyPI 安装为库，提供详细文档及开箱即用的 SOTA 强化学习结果复现示例。