
---
title: MiroThinker
---

### [MiroMindAI MiroThinker](https://github.com/MiroMindAI/MiroThinker)  ![GitHub Repo stars](https://img.shields.io/github/stars/MiroMindAI/MiroThinker?style=social)

**项目核心内容总结：**  
MiroThinker 是一个开源 AI 代理工具，支持通过大模型（如 Qwen3、GPT-5）和多工具集成（如 Google 搜索、网页抓取、代码执行）完成复杂任务。其核心功能包括：  
1. **任务执行**：通过配置 API 密钥（如 Serper、Jina、E2B）调用外部工具，支持搜索、数据抓取、代码运行等。  
2. **评估与优化**：提供基准测试脚本（如 HLE、GAIA、AIME2025），支持多轮对话上下文管理（256K 上下文长度），可监控评估进度。  
3. **可扩展性**：支持不同规模模型（如 8B/30B/235B）和上下文长度（128K/256K），通过调整参数（如 `MAX_CONTEXT_LENGTH`）优化内存使用。  

**使用方法**：  
- 安装依赖并配置 `.env` 文件中的 API 密钥。  
- 运行评估脚本（如 `uv run benchmarks/evaluate.py`）或收集追踪数据（如 `bash collect-trace.sh`）。  
- 通过进度监控脚本（如 `check_progress_<benchmark>.py`）查看任务状态。  

**主要特性**：  
- 支持大模型与长上下文（256K），提升复杂任务处理能力。  
- 集成多工具（搜索、代码执行、摘要生成），增强功能灵活性。  
- 提供性能优化方案（如减少并发任务数、使用较小模型版本）。  
- 开源 MIT 许可，社区驱动，支持多语言（中文/英文）文档和 Discord 社区支持。