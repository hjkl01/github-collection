
---
title: pytorch-image-models
---

### [huggingface pytorch-image-models](https://github.com/huggingface/pytorch-image-models)  ![GitHub Repo stars](https://img.shields.io/github/stars/huggingface/pytorch-image-models?style=social)

PyTorch Image Models (timm) 是一个集成了图像模型、层、优化器、调度器、数据增强及参考训练脚本的 PyTorch 工具库，旨在整合广泛的最先进模型并支持 ImageNet 训练结果复现。其核心功能包括：提供数十种 SOTA 架构（如 ViT、ConvNeXt、EfficientNet、ResNet 等）的模型实现与预训练权重，支持特征提取、分类头修改及统一 API 配置；内置多种优化器（AdamW、Lion、Muon 等）、学习率调度器及增强策略，提供高性能训练、验证及推理脚本，支持多 GPU 分布式、混合精度训练及 ONNX 导出；持续集成最新架构（如 NaFlexViT、MobileNetV5、SigLIP-2）及算法，适配动态分辨率与设备初始化。代码采用 Apache 2.0 许可，预训练权重基于 ImageNet 数据集。