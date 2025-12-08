
---
title: open-notebook
---

### [lfnovo open-notebook](https://github.com/lfnovo/open-notebook)

**项目核心内容总结：**

Open Notebook 是一款基于 AI 的研究管理工具，支持多模型（如 OpenAI、Anthropic、Ollama 等）的智能笔记、文档处理和对话交互。其核心功能包括：  
1. **研究管理**：通过“来源-笔记-聊天”三栏界面，实现资料整理、AI 生成笔记及基于内容的智能对话。  
2. **高级功能**：支持播客生成（多语音）、内容转换（摘要/提取）、REST API 接口及密码保护。  
3. **技术架构**：采用 Python（FastAPI）、Next.js/React 前端、SurrealDB 数据库，提供全面的开发文档。  

**使用方法**：  
- 通过 Docker 或 Docker Compose 部署，配置环境变量及数据库连接。  
- 支持直接运行（需手动安装依赖）。  

**主要特性**：  
- 多 AI 模型兼容，支持推理模型（如 DeepSeek-R1）。  
- 提供细粒度的上下文控制、引用标注及跨项目资源共享。  
- 开发者可利用 REST API 实现定制化集成，支持异步处理和实时更新。