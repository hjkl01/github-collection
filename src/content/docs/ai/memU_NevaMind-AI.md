
---
title: memU
---

### [NevaMind-AI memU](https://github.com/NevaMind-AI/memU)  ![GitHub Repo stars](https://img.shields.io/github/stars/NevaMind-AI/memU?style=social)

**项目核心内容总结：**  
memU 是一个用于提取和组织 AI 记忆的工具，支持处理多轮对话、日志和多模态数据（如文档、图像）。其核心功能包括：  
1. **分层记忆结构**：将信息组织为类别（如偏好、工作习惯）、项目（具体记忆点）和原始资源（如对话文件）。  
2. **双检索模式**：  
   - **RAG（检索增强生成）**：快速检索，支持跨层级搜索（类别→项目→资源），输出带相似度评分。  
   - **LLM（大模型推理）**：深度理解上下文，自动优化查询，按需停止检索。  
3. **使用方法**：  
   - 通过 Python 脚本处理数据（如 `example_1_conversation_memory.py` 处理对话文件，生成 Markdown 格式记忆分类）。  
   - 提供云服务（memU Cloud）和自托管服务（memU-server）。  
4. **主要特性**：  
   - 支持多模态内容统一管理（如文档与图像混合处理）。  
   - 高性能：在 Locomo 基准测试中平均准确率达 92.09%。  
   - 生态系统包含后台服务（memU-server）、可视化界面（memU-ui）及合作伙伴（如 Milvus、OpenAgents 等）。  

**适用场景**：个人 AI 助手、客服机器人、知识管理、研发团队技能提取等。