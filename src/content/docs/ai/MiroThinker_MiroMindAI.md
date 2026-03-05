
---
title: MiroThinker
---

### [MiroMindAI MiroThinker](https://github.com/MiroMindAI/MiroThinker)  ![GitHub Repo stars](https://img.shields.io/github/stars/MiroMindAI/MiroThinker?style=social)

MiroThinker 是 MiroMindAI 开发的开源深度研究代理，专为研究与预测任务优化。项目由 MiroThinker（核心代理）、MiroFlow（工具使用框架）和 MiroVerse（训练数据集）组成。

核心功能：
1. **深度推理能力**：支持 256K 上下文窗口，每任务最多 600 次工具调用，采用“交互扩展”技术提升性能。
2. **丰富工具链**：集成网页搜索、代码沙盒执行、多模态识别、文档解析等工具，支持自定义配置。
3. **多规格模型**：提供 8B 至 235B 多种参数量级模型，平衡性能与计算资源。
4. **全面评估体系**：内置支持 GAIA、HLE、BrowseComp 等多项基准评测，提供轨迹收集以辅助模型训练（SFT/DPO）。
5. **灵活部署**：基于 Python 生态，支持本地服务器（SGLang/vLLM）部署及 API 调用。

在 GAIA 等基准测试中达到开源 SOTA 水平，适用于需要复杂搜索与推理的科研及应用场景。