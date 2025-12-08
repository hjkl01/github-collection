
---
title: LMCache
---

### [LMCache LMCache](https://github.com/LMCache/LMCache)

LMCache 是一个用于优化大语言模型（LLM）推理性能的缓存系统，主要功能是通过存储和复用键值（KV）缓存，减少首次生成令牌时间（TTFT）并提高吞吐量，尤其适用于长上下文场景。其核心特性包括：  
1. **高效缓存管理**：支持将 KV 缓存存储在 GPU、CPU 内存、本地磁盘等多类型存储中，并可跨不同服务实例复用任意文本的缓存（不限于前缀）。  
2. **性能优化**：与 vLLM 集成后，可实现 3-10 倍的延迟降低和 GPU 资源节省，适用于多轮对话、RAG 等场景。  
3. **兼容性**：支持与 vLLM、SGLang 等框架集成，并兼容 CPU、磁盘及 NIXL 等存储方案。  

**使用方法**：通过 `pip install lmcache` 安装，详细用法可参考官方文档中的快速入门示例。  
**许可证**：采用 Apache License 2.0 协议。