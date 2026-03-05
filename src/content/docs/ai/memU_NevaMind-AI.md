
---
title: memU
---

### [NevaMind-AI memU](https://github.com/NevaMind-AI/memU)  ![GitHub Repo stars](https://img.shields.io/github/stars/NevaMind-AI/memU?style=social)

memU 是专为 24/7 持续运行 AI 代理设计的主动记忆框架，旨在降低长期运行的 LLM 令牌成本，使代理能够“永不遗忘”并主动行动。

**核心特性：**
1. **主动意图捕捉**：持续监测交互，无需指令即可理解用户目标、偏好及上下文，并主动执行任务。
2. **文件系统式记忆**：将记忆结构化存储（分类、条目、链接），支持分层浏览、即时挂载资源及持久化传输。
3. **双模式检索**：结合 RAG 的快速上下文组装与 LLM 的深度意图推理，支持实时建议与复杂预测。
4. **持续学习管道**：通过 `memorize()` 和 `retrieve()` API 实现零延迟处理、自动分类及跨会话知识累积。
5. **高兼容性与成本优化**：支持多种大模型（OpenAI、OpenRouter 等）及嵌入服务，通过缓存洞察显著减少 Token 消耗。

适用于信息推荐、邮件管理、交易监控及自我改进代理等场景。提供云端服务与自托管方案（Python 3.13+），包含完整 API 及多模态支持。