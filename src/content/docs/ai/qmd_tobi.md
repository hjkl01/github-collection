
---
title: qmd
---

### [tobi qmd](https://github.com/tobi/qmd)  ![GitHub Repo stars](https://img.shields.io/github/stars/tobi/qmd?style=social)

QMD 是一款本地运行的智能搜索引擎，专为检索 Markdown 笔记、会议记录和知识库文档设计。

核心功能：
- 混合检索：结合 BM25 全文搜索、向量语义搜索及 LLM 重排序，支持关键词与自然语言查询
- 本地运行：所有模型均在本地通过 GGUF 运行，保障数据隐私
- 上下文管理：支持为集合和路径添加描述性上下文，提升检索相关性
- 代理集成：提供 MCP 服务器及 JSON 输出，可直接集成至 Agent 工作流及 Claude 系列工具
- 命令行工具：支持集合管理、文档索引、嵌入生成及多格式导出