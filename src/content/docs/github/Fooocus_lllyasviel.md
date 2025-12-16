
---
title: Fooocus
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/lllyasviel/Fooocus?style=social) ](https://github.com/lllyasviel/Fooocus)
### [lllyasviel Fooocus](https://github.com/lllyasviel/Fooocus)

**核心内容总结：**  
Fooocus 是一个基于 Stable Diffusion 的图像生成工具，支持自定义模型、LoRA 微调、wildcards（随机词库）、数组处理等高级功能。用户可通过运行预设的 `run_anime.bat` 或 `run_realistic.bat` 快速启动不同风格的图像生成任务，或通过命令行参数灵活配置模型路径、采样器（如 `dpmpp_2m`）、硬件加速（如指定 GPU 设备 ID）等。项目提供配置文件（`config.txt`）供用户修改默认参数，支持多语言界面（需手动添加语言文件）。主要特性包括：  
- 支持多种模型加载与自定义路径管理；  
- 内置 wildcards 和数组处理，实现批量生成与随机元素替换；  
- 兼容 LoRA 模型，增强图像细节控制；  
- 提供丰富的命令行参数，适配不同硬件和性能需求；  
- 支持多语言界面，可扩展自定义翻译。  

**注意事项：**  
- 项目依赖 GPU 运行，需提前安装 CUDA 和相关库；  
- 修改配置文件前需备份，避免配置错误导致功能异常；  
- 部分高级功能（如 ControlNet）需额外安装模型文件；  
- 使用 wildcards 和数组处理时，需确保文件路径正确且格式符合要求。