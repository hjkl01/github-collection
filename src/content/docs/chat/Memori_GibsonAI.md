
---
title: Memori
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/GibsonAI/Memori?style=social) ](https://github.com/GibsonAI/Memori)
### [GibsonAI Memori](https://github.com/GibsonAI/Memori)

**项目核心内容总结**  
Memori 是一款为企业 AI 提供记忆管理的工具，支持与主流 LLM（如 OpenAI、Anthropic、Gemini 等）、数据库（如 PostgreSQL、MySQL、MongoDB 等）及框架（如 LangChain）无缝集成，无需修改现有架构。  

**主要功能**  
- **记忆管理**：自动记录 LLM 交互的上下文，支持跨会话的语义搜索与记忆召回。  
- **灵活集成**：支持多种 LLM、数据库和框架，提供统一接口（如 `Memori().openai.register()`）。  
- **高级增强**：通过属性、事件、关系等维度增强记忆，提升上下文准确性（需 API 密钥解锁更高限额）。  

**使用方法**  
1. 安装：`pip install memori`  
2. 初始化：配置 LLM（如 OpenAI）、数据库（如 SQLite）及 Memori 实例。  
3. 关键操作：  
   - 设置归属信息：`mem.attribution(entity_id="123", process_id="my-bot")`  
   - 会话管理：`mem.new_session()` 或 `mem.set_session()`  
   - 数据库配置：`Memori(conn=db_session_factory).config.storage.build()`  

**核心特性**  
- **高性能**：线程化处理、向量化记忆、零延迟提取。  
- **自动化**：单行代码初始化、自动模式迁移、CLI 工具（如 `python -m memori quota` 管理配额）。  
- **兼容性**：支持主流数据库（包括 Django ORM、SQLAlchemy）、异步/同步调用及多种 LLM 接口。