
---
title: LMCache
---

### [LMCache LMCache](https://github.com/LMCache/LMCache)  ![GitHub Repo stars](https://img.shields.io/github/stars/LMCache/LMCache?style=social)

LMCache 是一个大语言模型（LLM）推理服务扩展引擎，旨在降低首字延迟（TTFT）并提高吞吐量，尤其适用于长上下文场景。它通过将可复用文本的 KV 缓存存储在全数据中心（包括 GPU、CPU、磁盘、S3 等），并利用多种加速技术，实现跨推理实例的 KV 缓存复用。LMCache 支持与 vLLM、SGLang 等推理框架集成，提供 CPU KVCache 卸载、分离预填充、P2P KVCache 共享等功能，通过节省 GPU 周期来降低用户响应延迟。