### [Mano-P](https://github.com/Mininglamp-AI/Mano-P) ![GitHub Repo stars](https://img.shields.io/github/stars/Mininglamp-AI/Mano-P?style=social)

Mano-P 1.0 是一个面向边缘设备的开源 GUI-VLA（视觉-语言-动作）智能体项目，主打“私有 AI”，可在 Apple Silicon 设备本地运行，通过纯视觉理解完成跨应用 GUI 自动化操作。其核心功能包括：复杂界面自动操作、跨系统数据整合、长流程任务规划执行、自动化报告生成，以及端侧推理加速与自动化软件构建。

项目提供两种主要使用形态：  
1) **mano-cua 命令行工具**：支持自然语言驱动 GUI 自动化，具备云端/本地双推理模式；本地模式下截图与任务数据不出设备。  
2) **mano-skill（ClawHub Skill）**：供 Claude Code/OpenClaw 等智能体在推理过程中自动调用，实现多步骤任务自动执行。

技术上，Mano-P 基于 Mano-Action 双向自强化训练框架与三阶段训练流程，并针对端侧做了量化、剪枝和推理适配优化。配套 **Cider 推理 SDK** 补齐 MLX 缺失的 W8A8/W4A8 激活量化能力，在 Apple Silicon 上显著提升预填充性能，同时保持本地部署与隐私安全。

性能方面，Mano-P 在 GUI 智能体基准中表现领先（如 OSWorld 专项模型第一），支持在 Mac mini/MacBook（M4+、32GB+）或算力棒上部署，适用于高安全场景下的企业流程自动化、应用开发测试闭环（Mano-AFK）及日常交互任务。