### [google langextract](https://github.com/google/langextract)  ![GitHub Repo stars](https://img.shields.io/github/stars/google/langextract?style=social)

LangExtract 是一个基于大语言模型（LLM）的 Python 库，用于根据用户自定义指令从非结构化文本中提取结构化信息。核心功能包括：

1. **精确溯源**：将提取结果映射到源文本精确位置，支持可视化高亮与验证。
2. **结构化输出**：利用 few-shot 示例强制执行一致输出模式，确保符合预定义 Schema。
3. **长文档优化**：采用文本分块、并行处理及多次遍历策略，高效处理大规模文本。
4. **交互式可视化**：自动生成独立 HTML 文件，便于在原始上下文中审查提取实体。
5. **灵活模型支持**：支持云端（Gemini、OpenAI）及本地（Ollama）模型，支持自定义插件，无需微调。