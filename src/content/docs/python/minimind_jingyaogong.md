
---
title: minimind
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/jingyaogong/minimind?style=social) ](https://github.com/jingyaogong/minimind)
### [jingyaogong minimind](https://github.com/jingyaogong/minimind)

**项目核心内容总结：**  
MiniMind 是一个用于训练和评估小型语言模型（LLM）的开源项目，提供从零开始构建模型的完整方案。其核心功能包括：  
1. **模型训练与评估**：支持使用中文数据集训练模型，并通过 `lm_eval` 等工具评估模型在多个基准测试（如ceval、cmmlu）中的性能，指标包括准确率和推理速度。  
2. **多框架部署**：提供多种推理框架的集成方案，包括 Ollama（支持一键启动模型）、MNN（端侧推理引擎）及第三方工具（如 vllm、transformers），适配不同场景需求。  
3. **轻量化与高效性**：模型参数量从百万级到十亿级可选，支持 4-bit 量化和 MoE（混合专家）架构，兼顾性能与部署效率。  
4. **完整工具链**：包含数据预处理、训练脚本、模型导出及部署示例，支持从训练到推理的全流程。  

**使用方法**：  
- **训练**：通过 `train.py` 脚本配置数据路径、模型规模及训练参数，支持中文预训练和指令调优。  
- **评估**：运行 `lm_eval` 命令，指定模型路径和测试集，输出准确率等指标。  
- **部署**：使用 Ollama 一键启动模型（如 `ollama run minimind2`），或通过 MNN 导出量化模型并运行于端侧设备。  

**主要特性**：  
- 支持多种模型架构（如 MoE、小型化 Transformer）。  
- 提供中文优化方案，适配国内数据集与应用场景。  
- 开源且文档详实，包含训练步骤、推理示例及社区贡献内容。