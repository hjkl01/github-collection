### [whichllm](https://github.com/Andyyyy64/whichllm) ![GitHub Repo stars](https://img.shields.io/github/stars/Andyyyy64/whichllm?style=social)

whichllm 是一个命令行工具，用于根据你的硬件条件（GPU/CPU/内存）自动推荐“真正跑得动且综合表现最好”的本地大模型，而不是只按参数大小判断是否能装下。它会抓取 HuggingFace 实时模型数据，结合多来源基准测试（如 LiveBench、Arena ELO 等）进行证据分级打分，并综合显存适配、推理速度、量化方式、模型新旧代际、可信度等因素输出排名。

核心功能包括：自动硬件检测、GPU 模拟选型（购买前预估）、模型推荐与排序、升级对比（不同显卡方案）、反向规划（某模型需要什么硬件）、一键运行聊天（run）、生成可直接复制的 Python 推理代码（snippet）、JSON 输出便于脚本集成。支持 GGUF、AWQ/GPTQ、FP16/BF16 等格式，并内置缓存与离线回退机制。