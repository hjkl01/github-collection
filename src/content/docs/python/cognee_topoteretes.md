
---
title: cognee
---

### [topoteretes cognee](https://github.com/topoteretes/cognee)

**项目核心内容总结**  

**功能**  
Cognee 是一个开源工具，将原始数据转化为 AI 代理的持久化动态记忆，结合向量搜索与图数据库，实现文档的语义搜索与关系连接。提供自托管（本地部署）和云托管（Cognee Cloud）两种模式。  

**主要特性**  
- **自托管版本**：支持多种数据类型（对话、文件、音频等），替代传统 RAG 系统，提供模块化数据管道、高自定义任务及搜索接口。  
- **云托管版本**：提供网页仪表盘、自动更新、资源分析及企业级安全功能。  

**使用方法**  
1. **安装**：通过 pip、poetry 等工具安装，需配置 LLM API 密钥（如 OpenAI）。  
2. **运行流程**：通过 Python 脚本或 CLI 命令添加数据、生成知识图谱、查询结果。例如：  
   ```python  
   await cognee.add("文本")  
   await cognee.cognify()  
   await cognee.memify()  
   results = await cognee.search("查询")  
   ```  
3. **CLI 操作**：支持添加数据、生成图谱、搜索及删除数据等命令。  

**其他**  
- 提供 Colab 示例教程，支持多语言文档（如中文、英文等）。  
- 社区支持贡献、代码规范及研究论文引用（arXiv:2505.24478）。