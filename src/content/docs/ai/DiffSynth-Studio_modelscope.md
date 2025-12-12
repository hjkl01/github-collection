
---
title: DiffSynth-Studio
---

### [modelscope DiffSynth-Studio](https://github.com/modelscope/DiffSynth-Studio)

**项目核心内容总结**  
DiffSynth-Studio 是一个集成多种创新技术的 AI 图像与视频生成平台，提供统一架构支持图像理解、生成与编辑，包含以下核心功能：  
1. **Nexus-Gen**：通过共享嵌入空间实现图像理解、生成与编辑的统一模型，支持复杂任务。  
2. **ArtAug**：增强图像生成的美学表现，提供风格化渲染效果。  
3. **EliGen**：支持区域级精确控制，实现图像分区生成与编辑。  
4. **ExVideo**：扩展视频生成模型能力，提升参数效率与视频质量。  
5. **Diffutoon**：高分辨率动漫风格视频渲染，支持可编辑的卡通着色。  
6. **DiffSynth**：原始项目，实现视频合成中的防闪烁技术。  

**使用方法**  
- 通过 ModelScope 或 HuggingFace 获取预训练模型（如 LoRA、FLUX.1-dev 等）。  
- 使用在线工作室（如 ModelScope Nexus-Gen Studio）直接体验生成与编辑功能。  
- 参考示例代码（如 FLUX.1-dev-EliGen.py）进行本地部署与定制开发。  

**主要特性**  
- 支持多模态任务（生成、编辑、理解）的统一架构。  
- 提供高分辨率、风格化渲染及区域级控制能力。  
- 通过参数高效微调技术扩展模型应用范围。  
- 集成多项创新算法（如防闪烁、美学增强、实体级控制）。