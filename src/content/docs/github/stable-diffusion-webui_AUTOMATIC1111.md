
---
title: stable-diffusion-webui
---

### [AUTOMATIC1111 stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)

**项目核心内容总结：**

**项目功能**  
Stable Diffusion Web UI 是一个基于 Gradio 的 Stable Diffusion 图像生成工具，支持文本到图像（txt2img）、图像到图像（img2img）、修复、上色、风格迁移等操作，并提供参数保存、种子控制、批量处理、模型合并等功能。集成多种图像处理工具（如 GFPGAN、RealESRGAN）和高级功能（如文本反转、可编辑提示词、多模型兼容）。

**主要特性**  
- 支持 Stable Diffusion 1.x/2.x、Alt-Diffusion 等模型  
- 提供图像修复、扩展、超分、风格化等工具  
- 可保存生成参数、历史记录及模型权重  
- 支持自定义脚本扩展、API 调用及多平台部署  
- 优化性能（如 xformers 加速、内存高效注意力机制）  

**使用方法**  
1. **Windows**：下载仓库后运行 `webui-user.bat`  
2. **Linux**：通过 `webui.sh` 脚本安装依赖并启动  
3. **Mac**：按 Apple Silicon 指南安装（需 Rosetta 2）  
4. **在线部署**：支持 Google Colab 等云平台  
5. 安装时需确保 Python 3.10+/依赖库（如 libgl1）  

**其他**  
- 依赖库许可证信息可在 `Settings -> Licenses` 查看  
- 支持中文社区贡献（通过 Wiki 文档）