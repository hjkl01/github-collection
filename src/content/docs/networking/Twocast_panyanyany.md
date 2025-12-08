
---
title: Twocast
---

### [panyanyany Twocast](https://github.com/panyanyany/Twocast)

**核心内容总结：**  
Twocast 是一个 AI 生成双人播客的工具，支持通过主题、链接、文档（doc/pdf/txt）或列表页（5-9分钟）一键生成 3-5 分钟的播客，内容包含音频、大纲和脚本，支持中英文等多语言，并可下载音频。  

**使用方法：**  
1. **本地部署**：启动依赖服务（如 Textract 和 FFMPEG）、配置环境变量、初始化数据库后运行项目。  
2. **Docker 一键启动**：配置环境变量后通过 `docker compose up` 启动。  

**主要特性：**  
- 支持 Fish Audio、Minimax、Google Gemini 三大平台的语音合成（TTS）。  
- 需配置 TTS 和 LLM（如 OpenRouter、x.ai）的 API 密钥以启用功能。