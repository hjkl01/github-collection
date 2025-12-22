
---
title: langextract
---

### [google langextract](https://github.com/google/langextract)  ![GitHub Repo stars](https://img.shields.io/github/stars/google/langextract?style=social)

**项目核心内容总结：**

**功能**  
LangExtract 是一个信息提取工具，支持从文本中提取结构化数据（如医学信息、长文档内容），兼容多种模型（如 Gemini、OpenAI、本地 Ollama 模型），并提供自定义模型插件扩展功能。

**使用方法**  
1. 安装：通过 pip 安装基础包或 Docker 镜像。  
2. 配置 API 密钥（如 Gemini、OpenAI）或本地模型（如 Ollama）。  
3. 调用 `lx.extract()` 方法，指定文本、提取规则（prompt）、示例数据及模型参数。  

**主要特性**  
- 支持长文档处理（如《罗密欧与朱丽叶》全文提取）。  
- 结构化输出（如医学信息提取）。  
- 多模型兼容：云模型（Gemini/OpenAI）与本地模型（Ollama）。  
- 可扩展：通过插件系统添加自定义模型提供者。  
- 社区支持：提供社区插件库（如 RadExtract 医学报告结构化示例）。  

**注意事项**  
- 医疗相关功能仅用于演示，不可用于实际医疗诊断。  
- 需遵守 Apache 2.0 许可证及健康 AI 开发条款。