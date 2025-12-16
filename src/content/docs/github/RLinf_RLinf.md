
---
title: RLinf
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/RLinf/RLinf?style=social) ](https://github.com/RLinf/RLinf)
### [RLinf RLinf](https://github.com/RLinf/RLinf)

**项目核心内容总结：**  
RLinf 是一个高效的大规模强化学习（RL）框架，专注于提供灵活且可扩展的训练解决方案。其核心功能包括：  
1. **数学推理能力**：在 AIME 24、AIME 25 和 GPQA-diamond 等基准测试中，1.5B 和 7B 模型均表现优异，达到 SOTA 水平。  
2. **系统级增强**：支持异构 GPU、混合专家（MoE）架构、vLLM 推理后端，以及异步流水线执行。  
3. **应用级扩展**：涵盖视觉语言模型（VLMs）训练、多智能体训练、与仿真器（如 RoboCasa、GENESIS）集成，支持世界模型和现实 RL 背景智能。  
4. **稳定性保障**：提供全面的 CI 测试，覆盖单元测试和端到端训练流程。  

**使用方法**：  
用户需配置环境并安装依赖，通过训练脚本启动模型训练，利用框架支持的硬件加速和模型架构（如 MoE、vLLM）进行高效训练。  

**主要特性**：  
- 支持多种模型规模（1.5B/7B）及复杂训练场景（如多智能体、VLA）。  
- 系统级优化提升训练效率，应用级扩展覆盖视觉语言、仿真交互等场景。  
- 开源社区活跃，提供详细的贡献指南和论文引用。