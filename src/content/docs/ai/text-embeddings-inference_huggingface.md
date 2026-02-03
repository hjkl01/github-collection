
---
title: text-embeddings-inference
---

### [huggingface text-embeddings-inference](https://github.com/huggingface/text-embeddings-inference)  ![GitHub Repo stars](https://img.shields.io/github/stars/huggingface/text-embeddings-inference?style=social)

**项目核心内容总结**

**项目名称**：Text Embeddings Inference (TEI)

**项目功能**：  
TEI 是一个高性能的开源工具包，用于部署和提供文本嵌入模型和序列分类模型的推理服务。支持多种主流模型（如 BERT、XLM-RoBERTa、Qwen、GTE 等），适用于文本嵌入、重排序（re-ranking）、情感分析等任务。支持 REST API 和 gRPC 接口，具备生产级功能（如分布式追踪、Prometheus 监控、私有模型部署等）。

**主要特性**：
- 高性能推理：支持 Flash Attention、Candle、cuBLASLt 等优化技术；
- 支持多种模型架构：包括 BERT、XLM-RoBERTa、Mistral、GTE、JinaBERT、MPNet 等；
- 支持多种任务：文本嵌入、重排序、序列分类；
- 支持多种硬件：CPU、CUDA GPU（包括 Ampere、Hopper、Turing 等架构）、Apple M1/M2；
- 支持私有模型和网关模型部署；
- 支持分布式追踪（OpenTelemetry）、Prometheus 指标；
- 支持 REST API 和 gRPC 接口；
- 支持动态批处理（token-based batching）；
- 支持 SPLADE 池化方法；
- 支持 Docker 部署，提供多种架构的镜像；
- 支持本地安装，基于 Rust 实现，支持 CPU 和 CUDA。

**使用方法**：
1. **Docker 部署**：
   - 拉取镜像并运行容器，指定模型 ID；
   - 示例：`docker run --gpus all -p 8080:80 ghcr.io/huggingface/text-embeddings-inference:1.8 --model-id Qwen/Qwen3-Embedding-0.6B`
   - 通过 `curl` 或 gRPC 调用 API：`curl 127.0.0.1:8080/embed -d '{"inputs":"..."}`

2. **本地安装**：
   - 安装 Rust；
   - 使用 `cargo install` 安装 TEI；
   - 支持 CPU 和 CUDA 后端；
   - 示例：`text-embeddings-router --model-id Qwen/Qwen3-Embedding-0.6B --port 8080`

3. **私有模型部署**：
   - 设置 `HF_TOKEN` 环境变量，使用私有模型；
   - 示例：`docker run -e HF_TOKEN=xxx --model-id my-private-model`

4. **API 接口**：
   - 提供 `/embed`（嵌入）、`/rerank`（重排序）、`/predict`（预测）等接口；
   - 支持 JSON 格式输入；
   - 支持 OpenAPI 文档，通过 `/docs` 访问。

**支持的模型**：
- 文本嵌入模型：如 Qwen3、GTE、XLM-RoBERTa、MPNet、NomicBERT 等；
- 重排序模型：如 BAAI/bge-reranker-large；
- 序列分类模型：如 SamLowe/roberta-base-go_emotions。

**部署建议**：
- 使用 Docker 镜像快速部署；
- 支持 GPU 加速（需安装 NVIDIA 容器工具包）；
- 支持离线部署（通过挂载模型文件）；
- 支持多种架构的镜像（如 CPU、Turing、Ampere、Hopper 等）。

**文档资源**：
- API 文档：Swagger UI 和 OpenAPI；
- 示例：提供部署和使用示例；
- MTEB 排行榜：用于选择最佳模型。