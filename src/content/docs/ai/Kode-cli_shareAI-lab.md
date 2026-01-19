
---
title: Kode-cli
---

### [shareAI-lab Kode-cli](https://github.com/shareAI-lab/Kode-cli)  ![GitHub Repo stars](https://img.shields.io/github/stars/shareAI-lab/Kode-cli?style=social)

**项目核心内容总结：**  
Kode 是一个支持多模型协作的 AI 开发工具，可管理多个大模型（如 Claude、Qwen、Gemini 等），实现任务分配、代码生成、架构设计等开发流程。  

**主要功能：**  
1. **多模型协作**：支持不同模型分工（如用 GPT-5 设计架构、Claude 优化代码），并行处理任务。  
2. **专家咨询**：临时调用特定专家模型（如 Grok 4）解决复杂问题。  
3. **任务分配工具**：通过 SubAgent 并行执行多个子任务，提升效率。  
4. **成本跟踪**：实时统计各模型的 token 使用量和费用。  

**使用方法：**  
- 安装 Bun 工具，克隆代码后执行 `bun install` 和 `bun run dev` 启动开发环境。  
- 通过命令行（如 `/model` 切换模型、`/cost` 查看费用）或配置文件管理模型参数。  
- 支持 AGI 类似 API 端点接入自定义模型。  

**核心特性：**  
- 灵活切换模型（Tab 键快速切换，`/model` 配置默认模型）。  
- 上下文管理：切换模型时保持对话连贯性。  
- 多模型协作优势：结合不同模型的强项（如架构设计、代码生成、复杂推理）。