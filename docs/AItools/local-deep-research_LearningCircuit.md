### [local-deep-research](https://github.com/LearningCircuit/local-deep-research) ![GitHub Repo stars](https://img.shields.io/github/stars/LearningCircuit/local-deep-research?style=social)

Local Deep Research 是一款可本地部署、可控的 AI 深度研究助手：通过多种大模型与搜索引擎自动执行研究任务，整合网页、学术数据库和本地文档信息，生成带规范引用的摘要与报告。它支持 20+ 研究策略（含自主决策的 LangGraph Agent）、多种研究模式（快速摘要/深度研究/报告生成/文档分析）、研究历史管理、实时进度更新、PDF/Markdown 导出，以及面向订阅场景的自动研究简报。

项目核心能力还包括：将研究来源下载到个人加密知识库，自动抽取、索引和检索，实现“私有资料+实时网络”联合问答；支持本地与云端 LLM（Ollama、LM Studio、llama.cpp、OpenAI、Anthropic、Gemini、OpenRouter 等）；提供 Python API、HTTP API、CLI、MCP（Claude 集成）和 LangChain 检索器集成，便于企业接入现有向量库与知识系统。

在隐私与安全方面，项目强调本地优先与数据主权：无遥测、无追踪、无分析上报；每用户独立 SQLCipher（AES-256）加密数据库；支持全本地运行（如 Ollama + SearXNG）；并配套完善的供应链与代码安全扫描体系。性能上，项目公布了本地硬件上的较高基准结果（如 SimpleQA 约 95%）。