
---
title: LTX-Video
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/Lightricks/LTX-Video?style=social) ](https://github.com/Lightricks/LTX-Video)
### [Lightricks LTX-Video](https://github.com/Lightricks/LTX-Video)

**项目核心内容总结：**  
LTX-Video 是一个基于潜在扩散模型的实时视频生成工具，支持高分辨率视频生成（如 720x480x121）和多种控制模型（姿势、深度、边缘控制）。项目提供 2B/13B 参数量模型及 8-bit 优化版本，适配 NVIDIA ADA 显卡，生成速度提升 3 倍。  

**主要功能与特性：**  
1. **生成能力**：支持高分辨率视频生成，兼容 ComfyUI 插件及 Diffusers 库，提供自动提示词优化功能。  
2. **控制模型**：集成姿势、深度、边缘控制模型，实现精准生成。  
3. **性能优化**：8-bit 版本（LTX-VideoQ8）及 TeaCache 技术（加速 2 倍）提升推理效率。  
4. **训练与微调**：开源训练框架支持 LoRA 微调及 Control LoRAs（如深度、姿态控制）。  

**使用方法：**  
- 通过 ComfyUI 插件、Diffusers 库或命令行工具调用模型。  
- 使用提示词工程（如详细动作描述、环境细节）生成视频。  
- 社区工具（如 ComfyUI-LTXTricks）提供高级功能（如 RF-Inversion、FlowEdit）。  

**其他：**  
项目提供开源训练代码及社区贡献的加速方案，适用于视频生成、AI 研究等场景。