
---
title: nvidia-container-toolkit
---

### [NVIDIA nvidia-container-toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)

**NVIDIA Container Toolkit 核心内容总结：**  
该项目提供了一套工具和库，用于构建和运行基于 GPU 的容器，使容器能够自动适配并利用 NVIDIA GPU 资源。主要功能包括：  
- 提供容器运行时库（libnvidia-container）和配置工具，实现 GPU 资源的自动识别与加载；  
- 支持 Docker 等容器平台，通过命令行参数配置 GPU 容器；  
- 需先安装 NVIDIA 驱动（无需安装 CUDA Toolkit），具体安装步骤见官方文档。  

**使用方法：**  
1. 确保系统已安装 NVIDIA 驱动；  
2. 参考官方安装指南部署 Toolkit；  
3. 通过 Docker 命令启用 GPU 支持（如 `--gpus all`）。  

**主要特性：**  
- 自动化 GPU 配置，简化容器部署流程；  
- 提供详细文档和社区支持，支持多平台；  
- 无需依赖 CUDA Toolkit，仅需 NVIDIA 驱动即可运行。