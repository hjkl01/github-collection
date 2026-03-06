
---
title: minimind
---

### [jingyaogong minimind](https://github.com/jingyaogong/minimind)  ![GitHub Repo stars](https://img.shields.io/github/stars/jingyaogong/minimind?style=social)

MiniMind 是一个从零开始训练超轻量级大语言模型（LLM）的开源项目，旨在通过极简架构和原生代码实现，降低个人设备训练 LLM 的门槛。

核心功能如下：
1. **极低成本训练**：仅需单卡 3090 及约 3 元人民币成本，2 小时内即可从 0 训练出 25.8M 参数的对话模型。
2. **全流程算法复现**：包含 Tokenizer 训练、预训练、指令微调（SFT）、LoRA、直接偏好优化（DPO）及强化学习（RLAIF: PPO/GRPO/SPO）等全过程，核心算法均基于 PyTorch 原生重构。
3. **多样模型架构**：支持 Dense 和混合专家（MoE）结构，具备长文本外推能力（YaRN 算法），并拓展了视觉多模态模型 MiniMind-V。
4. **完善工具生态**：提供清洗后的高质量开源数据集，兼容 transformers、vllm、llama.cpp 等主流框架，内置 OpenAI 协议 API 服务端及 Streamlit WebUI。

该项目适合作为 LLM 入门教程，帮助用户深入理解模型底层原理及构建全过程。