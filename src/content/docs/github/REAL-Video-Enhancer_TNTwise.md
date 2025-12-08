
---
title: REAL-Video-Enhancer
---

### [TNTwise REAL-Video-Enhancer](https://github.com/TNTwise/REAL-Video-Enhancer)

**项目功能**  
REAL Video Enhancer 是一款支持 Windows、Linux 和 macOS 的视频增强工具，提供帧插值（如 24FPS→48FPS）和超分辨率（如 1920×1080→3840×2160）功能，支持多种模型（如 RIFE、GMFSS、AnimeSR 等）。  

**使用方法**  
- 通过 Git 克隆代码，使用 PyInstaller（Windows/Mac）或 cx_Freeze（Linux）构建可执行文件。  
- 提供 Colab Notebook 用于云端处理。  

**主要特性**  
- 跨平台支持（Windows 10/11、macOS 14+、Ubuntu 22.04+）。  
- 集成 Discord RPC、场景变化检测。  
- 支持 TensorRT（NVIDIA GPU）、NCNN（Vulkan 兼容设备）等后端加速。  
- 提供多种插值模型（RIFE、GIMM 等）和超分模型（SPAN、Real-ESRGAN 等）。  
- 便携式 Python 后端，支持多平台移植。