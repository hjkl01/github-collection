### [kvcache-ai ktransformers](https://github.com/kvcache-ai/ktransformers)  ![GitHub Repo stars](https://img.shields.io/github/stars/kvcache-ai/ktransformers?style=social)

KTransformers 是一个基于 CPU-GPU 异构计算的大语言模型高效推理与微调框架，旨在释放混合计算在 MoE 模型中的潜力。项目核心功能包含以下模块：

*   **kt-kernel（高性能推理）**：提供 CPU 优化内核（支持 AMX/AVX 加速）、MoE 推理优化及量化支持（INT4/INT8/GPTQ），可与 SGLang 集成，实现大型 MoE 模型的 CPU-GPU 混合推理。
*   **kt-sft（微调框架）**：与 LLaMA-Factory 集成，支持超大规模 MoE 模型（如 671B DeepSeek-V3）的资源高效微调（LoRA），利用异构加速显著降低显存需求。
*   **广泛适配**：支持多种主流模型（DeepSeek, Kimi, Qwen, GLM 等）、多硬件平台（Intel, AMD, Ascend, Windows 等）及优化特性（FP8/BF16、长上下文、专家调度等）。