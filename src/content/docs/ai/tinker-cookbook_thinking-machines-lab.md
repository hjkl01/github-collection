
---
title: tinker-cookbook
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/thinking-machines-lab/tinker-cookbook?style=social) ](https://github.com/thinking-machines-lab/tinker-cookbook)
### [thinking-machines-lab tinker-cookbook](https://github.com/thinking-machines-lab/tinker-cookbook)

**核心内容总结：**  
该项目提供两个工具库（`tinker` 和 `tinker-cookbook`），用于定制化语言模型训练：  
1. **tinker** 是一个训练 SDK，通过 API 实现分布式训练，用户仅需发送请求即可完成模型微调。  
2. **tinker-cookbook** 包含多种训练场景的示例代码（如监督学习、强化学习、数学推理、对话优化等），基于 `tinker` 提供通用抽象层，简化训练流程。  

**使用方法：**  
- 注册获取 API 密钥，通过 `pip` 安装 `tinker` 和 `tinker-cookbook`。  
- 使用 `tinker` 提供的训练客户端（如 `forward_backward`、`optim_step`）进行模型训练，或通过 `tinker-cookbook` 中的示例代码（如 `sl_loop.py`、`rl_loop.py`）快速实现特定任务（如对话微调、奖励模型训练）。  
- 支持下载训练后的模型权重，并提供评估工具（如 `evaluation` 模块）对接标准基准测试。  

**主要特性：**  
- 提供从基础训练到复杂场景（如多智能体博弈、工具使用）的完整训练流程示例。  
- 内置实用工具，包括超参数计算、对话格式转换、模型评估等模块。  
- 支持通过 `tinker` 的 API 实现高效分布式训练，降低开发复杂度。