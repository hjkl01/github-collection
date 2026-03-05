
---
title: paperless-gpt
---

### [icereed paperless-gpt](https://github.com/icereed/paperless-gpt)  ![GitHub Repo stars](https://img.shields.io/github/stars/icereed/paperless-gpt?style=social)

**paperless-gpt** 是一款与 paperless-ngx 无缝集成的 AI 文档管理增强工具，核心功能如下：

*   **AI 增强 OCR**：利用大语言模型（如 OpenAI、Ollama）或云服务（Google Document AI、Azure Document Intelligence）进行高精度文字识别，显著优于传统 OCR，尤其适用于复杂布局或低质量扫描件。
*   **自动化元数据管理**：自动生成并建议文档标题、标签、对应方、自定义字段及创建日期，支持 Web 界面手动审核或自动应用。
*   **可搜索 PDF 生成**：创建带有透明文本层的 PDF 文件，实现文档内容可搜索、可选择，同时保留原始外观。
*   **高度可定制与扩展**：支持多种 LLM 和 OCR 提供商，提供 Web 界面自定义提示词（Prompts），允许本地保存处理结果或回传至 paperless-ngx。
*   **便捷部署**：基于 Docker，仅需配置少量环境变量即可快速部署并与 paperless-ngx 协同工作。