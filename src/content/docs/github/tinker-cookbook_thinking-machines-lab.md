
---
title: tinker-cookbook
---

### [thinking-machines-lab tinker-cookbook](https://github.com/thinking-machines-lab/tinker-cookbook)

**项目功能**  
Tinker Cookbook 提供两个核心工具：`tinker`（用于语言模型微调的训练SDK）和 `tinker-cookbook`（包含多种微调场景的示例和高级抽象）。  

**使用方法**  
1. 注册获取API密钥，安装Python客户端（`pip install tinker`）及cookbook（`pip install -e .`）。  
2. 通过API调用 `tinker` 提供的训练接口（如 `forward_backward`、`optim_step`）进行模型微调。  
3. 使用 `tinker-cookbook` 中的示例（如监督学习、强化学习、数学推理等）快速搭建训练流程。  

**主要特性**  
- **多样化训练场景**：支持对话微调、数学推理、偏好学习、工具使用、多智能体训练等。  
- **实用工具库**：提供超参数计算、模型评估、结构化数据渲染等功能。  
- **社区驱动**：开源项目，支持贡献代码，提供标准基准评估集成。