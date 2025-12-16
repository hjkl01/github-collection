
---
title: deepwiki-open
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/AsyncFuncAI/deepwiki-open?style=social) ](https://github.com/AsyncFuncAI/deepwiki-open)
### [AsyncFuncAI deepwiki-open](https://github.com/AsyncFuncAI/deepwiki-open)

**项目核心内容总结：**  
1. **功能**  
- 通过RAG技术实现代码仓库对话（Ask功能），基于代码内容生成精准回答；  
- DeepResearch功能支持多轮研究分析，提供结构化结论；  
- 集成OpenRouter，支持OpenAI、Anthropic、Google等多模型调用。  

2. **使用方法**  
- 通过API服务器实现仓库克隆、索引及RAG操作；  
- 支持Docker部署，提供`.env`文件配置API密钥及证书；  
- 前端界面支持私有仓库访问、模型切换及DeepResearch功能启用。  

3. **主要特性**  
- 支持GitHub/GitLab/Bitbucket私有仓库（需Token）；  
- 实时流式生成回答，维护对话上下文；  
- DeepResearch多轮研究（最多5轮迭代）；  
- 多模型集成（OpenRouter），灵活选择模型优化成本与性能。  

4. **其他**  
- 提供API服务器详细文档及故障排查指南；  
- 支持自签名证书部署及本地Docker镜像构建。