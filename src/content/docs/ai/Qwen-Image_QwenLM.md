
---
title: Qwen-Image
---

### [QwenLM Qwen-Image](https://github.com/QwenLM/Qwen-Image)  ![GitHub Repo stars](https://img.shields.io/github/stars/QwenLM/Qwen-Image?style=social)

### 项目核心内容总结：

Qwen-Image 是一个基于扩散模型的图像生成系统，具备强大的图像生成和编辑能力。其主要功能包括：

- **图像生成**：支持高质量的文本到图像生成，能够根据用户提供的文本描述生成逼真的图像。
- **图像编辑**：支持对已有图像进行修改，如调整光照、生成辅助线、替换材质等，适用于工业设计等专业场景。
- **LoRA 支持**：用户可以通过 LoRA（低秩适应）技术对模型进行微调，以生成个性化图像。
- **多平台支持**：已在 HuggingFace、ModelScope、SGLang、WaveSpeedAI、LiblibAI 等平台部署，用户可方便地使用这些平台进行图像生成和实验。

### 使用方法：

- 用户可通过 ModelScope 等平台的图像生成功能，输入提示词生成图像。
- 用户可通过 LoRA 训练功能，训练定制化的图像生成模型。
- 使用 SGLang 进行图像生成时，可直接调用 `sglang generate` 命令，结合图像和文本提示进行生成。

### 主要特性：

- **高性能**：支持低显存推理（如 4GB VRAM），以及 FP8 量化等优化技术。
- **工业级应用**：适用于工业产品设计、材质替换等专业场景。
- **多语言支持**：提供中文和英文的文档和社区支持。
- **开源与社区**：项目基于 Apache 2.0 协议开源，并在 GitHub 上持续更新和维护，支持用户反馈和贡献。

- **AI Arena**：提供一个公平、透明的模型评估平台，用户可参与模型评分，推动模型性能的持续优化。

### 社区支持：

- 用户可通过 Discord 和 WeChat 加入社区，与开发团队交流。
- 提交 GitHub Issues 或 Pull Requests，参与项目贡献。