
---
title: lerobot
---

### [huggingface lerobot](https://github.com/huggingface/lerobot)

**核心内容总结：**  
LeRobot 是一个基于 PyTorch 的机器人学习库，提供多种预训练策略（如扩散策略、ACT 策略等），适用于现实世界和模拟环境。用户可通过加载预训练模型快速部署，支持自定义训练和评估。主要特性包括：  
1. **功能**：涵盖机器人控制、多任务学习，支持 ALOHA、PushT、Simxarm 等环境，提供预训练模型和数据集。  
2. **使用方法**：安装后通过命令行工具加载模型（如 `lerobot-train`）、训练、评估，支持自定义配置和参数调整。  
3. **特性**：灵活的模型架构、支持视频和状态输入、统一数据格式（Parquet/MP4）、社区贡献模型可上传至 Hugging Face Hub。  
4. **扩展性**：支持添加新策略、数据集，提供详细贡献指南和评估脚本。