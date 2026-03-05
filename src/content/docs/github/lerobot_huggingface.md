
---
title: lerobot
---

### [huggingface lerobot](https://github.com/huggingface/lerobot)  ![GitHub Repo stars](https://img.shields.io/github/stars/huggingface/lerobot?style=social)

LeRobot 是 Hugging Face 推出的基于 PyTorch 的机器人库，旨在降低现实世界机器人开发的门槛。其核心功能包括：

1. **统一硬件控制接口**：提供硬件无关的 Python 原生接口，标准化多种机器人平台（从低成本机械臂到类人机器人）的控制与遥操作。
2. **标准化数据集**：采用 Parquet + 视频/图像格式，托管于 Hugging Face Hub，支持大规模数据集的高效存储、流式传输和可视化。
3. **先进模型与训练**：内置模仿学习、强化学习及 VLA 等 SOTA 策略，提供训练与评估脚本，支持实机部署及基准测试。
4. **高度可扩展性**：允许用户自定义机器人接口和策略，利用其数据收集、训练和可视化工具。