
---
title: evals
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/openai/evals?style=social) ](https://github.com/openai/evals)
### [openai evals](https://github.com/openai/evals)

### 核心内容总结  
**项目功能**：  
OpenAI Evals 是一个用于评估大型语言模型（LLM）或基于 LLM 的系统的框架，提供现有评估模板和自定义评估功能，支持使用私有数据构建评估，无需公开数据。  

**使用方法**：  
1. 设置 OpenAI API 密钥并安装 Python 3.9 及以上版本。  
2. 通过 Git-LFS 下载评估数据，或仅获取特定评估数据。  
3. 安装依赖项（`pip install -e .`），并使用 `pre-commit` 工具进行代码格式化。  
4. 运行评估（`pip install evals`），可选地将结果记录到 Snowflake 数据库。  

**主要特性**：  
- 提供多种评估模板（如提示链、工具代理等）。  
- 支持自定义评估逻辑和模型评分（YAML 文件）。  
- 可集成 Weights & Biases 进行可视化分析。  
- 强调数据隐私，允许使用私有数据构建评估。  
- 提供代码质量工具（如 `pre-commit`）。