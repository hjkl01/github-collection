### [graphify](https://github.com/safishamsi/graphify) ![GitHub Repo stars](https://img.shields.io/github/stars/safishamsi/graphify?style=social)

Graphify 是一款知识图谱构建工具，在 AI 编程助手中输入 `/graphify` 即可将整个项目（代码、文档、PDF、图片、视频）映射为可查询的知识图谱。

核心功能：解析 36+ 编程语言的 AST，提取代码结构和语义关系；支持文档、PDF、图片、音视频的语义提取。输出三个文件：`graph.html`（交互式可视化）、`GRAPH_REPORT.md`（关键概念、关联发现、建议问题）、`graph.json`（完整图谱随时查询）。

支持 Claude Code、Cursor、Codex、Kilo 等主流 AI 编程助手。可通过 CLI 直接查询图谱、查找路径、导出 Mermaid 调用流图。支持团队协作：提交 `graphify-out/` 后团队成员可直接使用。代码和音视频转录在本地处理，隐私友好。