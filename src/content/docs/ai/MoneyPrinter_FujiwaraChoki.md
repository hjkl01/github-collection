
---
title: MoneyPrinter
---

### [FujiwaraChoki MoneyPrinter](https://github.com/FujiwaraChoki/MoneyPrinter)  ![GitHub Repo stars](https://img.shields.io/github/stars/FujiwaraChoki/MoneyPrinter?style=social)

MoneyPrinter 是一款通过输入视频主题自动化生成 YouTube Shorts 的工具。

核心特点：
1. **本地 AI 生成**：脚本和元数据完全由本地 Ollama 模型驱动。
2. **队列处理**：基于 API、Worker 和 Postgres (Docker) 的数据库队列，保障处理可靠及重启安全。
3. **配置灵活**：支持交互式安装、Docker 部署，集成 ImageMagick 及 TikTok 会话配置。