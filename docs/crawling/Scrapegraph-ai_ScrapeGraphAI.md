### [Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) ![GitHub Repo stars](https://img.shields.io/github/stars/ScrapeGraphAI/Scrapegraph-ai?style=social)

ScrapeGraphAI 是一个基于 LLM（大语言模型）和图逻辑的 Python 网页抓取库，可从网页或本地文档（如 XML、HTML、JSON、Markdown）中按提示词自动提取结构化信息。用户只需描述想要的数据，系统即可生成并执行抓取流程。

项目提供多种抓取管线：
- **SmartScraperGraph**：单页抓取（最常用）
- **SearchGraph**：基于搜索引擎结果的多页抓取
- **SmartScraperMultiGraph**：多来源多页抓取
- **ScriptCreatorGraph / ScriptCreatorMultiGraph**：抓取并生成 Python 脚本
- **SpeechGraph**：抓取并生成音频输出  
并支持多版本并行调用 LLM 提升效率。

模型与生态支持广泛：可接入 OpenAI、Groq、Azure、Gemini、MiniMax 等 API 模型，也支持通过 Ollama 使用本地模型。除 Python 库外，还提供 API、Python/Node SDK，以及与 LangChain、LlamaIndex、CrewAI、Zapier、Bubble、Pipedream、n8n、Dify 等框架/低代码平台集成。项目采用 MIT 许可证。