
---
title: minimind
---

### [jingyaogong minimind](https://github.com/jingyaogong/minimind)  ![GitHub Repo stars](https://img.shields.io/github/stars/jingyaogong/minimind?style=social)

MiniMind 是一个从零训练超小语言模型的开源项目，旨在降低大模型学习门槛并推动社区进步。核心功能总结如下：

1. **极简训练成本**：单卡 NVIDIA 3090 环境下，仅需约 2 小时、3 元人民币即可训练出最小 25.8M 参数的语言模型。
2. **完整训练流程开源**：包含 Tokenizer 训练、预训练、监督微调 (SFT)、LoRA、强化学习 (DPO/PPO/GRPO/SPO) 及模型蒸馏全过程代码，核心算法均使用 PyTorch 原生从零重构。
3. **多样化模型支持**：支持 Dense 与混合专家 (MoE) 结构，拓展了视觉多模态 (VLM) 及推理模型。
4. **广泛兼容与部署**：兼容 transformers、llama.cpp、vllm、ollama 等主流框架，提供 OpenAI 协议 API 服务及 Streamlit WebUI 前端，支持长文本外推。