### [llmfit](https://github.com/AlexsJones/llmfit) ![GitHub Repo stars](https://img.shields.io/github/stars/AlexsJones/llmfit?style=social)

llmfit 是一个用于本地大语言模型选型与适配的终端工具，能够自动检测设备的 CPU、内存、GPU 与显存，根据模型质量、速度、内存适配度和上下文能力，为用户推荐真正适合本机运行的 LLM。它支持数百个模型与多种本地运行后端，包含多 GPU、MoE 架构识别、动态量化选择、推理速度估算，以及 Ollama、llama.cpp、MLX、Docker Model Runner、LM Studio 等集成。

项目提供交互式 TUI 和传统 CLI 两种使用方式，支持模型搜索、筛选、排序、对比、硬件模拟、硬件规划、下载管理、高级参数调优、社区实测性能排行榜和本地推理基准测试；同时支持 JSON 输出、REST API 服务、Web 仪表盘，以及通过手动覆盖硬件参数来模拟不同设备环境。其核心目标是帮助用户快速判断“自己的硬件最适合跑哪些模型，以及怎样跑得更好”。