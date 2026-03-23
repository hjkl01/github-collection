### [vllm-project vllm-omni](https://github.com/vllm-project/vllm-omni)  ![GitHub Repo stars](https://img.shields.io/github/stars/vllm-project/vllm-omni?style=social)

vLLM-Omni 是 vLLM 框架的扩展，专注于全模态（文本、图像、视频、音频）模型的高效推理与服务。它支持非自回归架构（如扩散 Transformer/DiT）及异构输出，利用高效 KV 缓存管理、流水线执行和完全解耦服务架构实现高性能。项目提供 Hugging Face 无缝集成、多种并行策略、流式输出及 OpenAI 兼容 API，兼容 GPU、ROCm、NPU、XPU 等多种硬件平台，支持 Qwen-Omni 等全模态及多模态生成模型部署。