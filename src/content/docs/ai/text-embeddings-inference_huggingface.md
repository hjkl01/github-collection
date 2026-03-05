
---
title: text-embeddings-inference
---

### [huggingface text-embeddings-inference](https://github.com/huggingface/text-embeddings-inference)  ![GitHub Repo stars](https://img.shields.io/github/stars/huggingface/text-embeddings-inference?style=social)

Text Embeddings Inference (TEI) 是一个高性能的开源文本嵌入及序列分类模型部署与推理工具包。它支持多种主流模型架构（如 Qwen、BERT、XLM-RoBERTa 等）及任务（嵌入、重排序、序列分类），集成 Flash Attention、Candle、ONNX 等优化技术，支持 GPU 及 Apple Silicon 本地加速。项目具备动态批处理、分布式追踪和生产级监控特性，支持通过 Docker、本地编译或 Homebrew 部署，并提供 REST API 和 gRPC 接口。