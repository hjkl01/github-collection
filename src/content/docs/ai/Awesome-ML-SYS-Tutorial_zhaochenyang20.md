
---
title: Awesome-ML-SYS-Tutorial
---

### [zhaochenyang20 Awesome-ML-SYS-Tutorial](https://github.com/zhaochenyang20/Awesome-ML-SYS-Tutorial)  ![GitHub Repo stars](https://img.shields.io/github/stars/zhaochenyang20/Awesome-ML-SYS-Tutorial?style=social)

该README文档主要介绍一个面向深度学习模型开发、训练与推理的综合性技术框架，包含以下核心内容：

**项目功能**  
1. 支持高性能模型推理（如SGLang引擎、vllm框架），涵盖量化（BF16/AWQ）、约束解码、在线权重更新等特性  
2. 提供分布式训练优化方案，包含Tensor Parallelism实现、NCCL通信优化、DP Attention机制等  
3. 集成模型服务系统（如Mooncake调度框架、ModelServer前端系统），支持P/D分离计算与多卡负载均衡  
4. 涵盖Transformer架构解析（如Cross-Attention机制）、CUDA图优化、特殊token处理等基础技术  

**使用方法**  
- 通过Docker管理开发环境，支持标准化部署流程  
- 提供Jupyter Notebook文档化编译与CI集成方案  
- 包含模型服务配置指南（如Embedding模型部署、Qwen3-Coder工具调用）  

**主要特性**  
- 高效推理：支持零开销批处理调度、Chunked Prefill分块预填充、Verl引擎优化  
- 灵活训练：实现从零构建张量并行、NCCL拓扑检测、PyTorch分布式通信（DDP/GIL优化）  
- 工程工具：提供内存泄漏分析（Torch内存快照）、量化架构设计分析、多节点推理框架（NVIDIA Dynamo）等实用模块