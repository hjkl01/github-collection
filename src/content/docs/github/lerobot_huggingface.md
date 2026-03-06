
---
title: lerobot
---

### [huggingface lerobot](https://github.com/huggingface/lerobot)  ![GitHub Repo stars](https://img.shields.io/github/stars/huggingface/lerobot?style=social)

LeRobot 是基于 PyTorch 的 Hugging Face 机器人库，旨在降低物理 AI 门槛，实现数据与模型的共享。主要功能包括：

1. **统一硬件接口**：提供硬件无关的 `Robot` 类，标准化多种机器人（如机械臂、人形机器人）及控制设备的连接与操作，支持自定义扩展。
2. **标准化数据集**：采用 Parquet 加视频的 LeRobotDataset 格式托管于 Hugging Face Hub，支持海量机器人数据的高效存储、流式读取、剪辑与合并。
3. **前沿策略模型**：内置模仿学习、强化学习及视觉语言动作（VLA）等 SOTA 模型，支持纯 PyTorch 训练、部署及模型共享。
4. **评估与基准**：提供统一评估脚本，支持仿真或实机测试，兼容 LIBERO、MetaWorld 等标准基准。
5. **开源生态支持**：提供完整文档、教程及社区支持，致力于工具链扩展与物理 AI 的民主化。