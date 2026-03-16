### [Tencent WeKnora](https://github.com/Tencent/WeKnora)  ![GitHub Repo stars](https://img.shields.io/github/stars/Tencent/WeKnora?style=social)

WeKnora 是一个基于大语言模型（LLM）的文档理解与检索框架，采用 RAG 架构，专为处理复杂异构文档设计。

**核心功能：**
*   **文档解析**：支持 PDF、Word、图片等多种格式，具备 OCR 及结构化内容提取能力。
*   **知识库管理**：支持 FAQ 和文档知识库，提供混合检索策略（关键词、向量、知识图谱）及跨库检索。
*   **Agent 智能体**：支持 ReACT 模式，可调用内置工具、MCP 工具及网页搜索，实现多轮对话与复杂推理。
*   **模型集成**：兼容本地模型（如 Ollama）和外部 API（如 Qwen、DeepSeek），支持灵活配置。
*   **部署与集成**：提供 Web 界面和 RESTful API，支持 Docker、Kubernetes 私有化部署，集成微信对话开放平台。
*   **安全机制**：支持登录认证，推荐内网部署以保障数据主权与安全。