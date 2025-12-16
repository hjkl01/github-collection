
---
title: agenticSeek
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/Fosowl/agenticSeek?style=social) ](https://github.com/Fosowl/agenticSeek)
### [Fosowl agenticSeek](https://github.com/Fosowl/agenticSeek)

**项目核心内容总结：**  
AgenticSeek 是一个本地运行的 AI 代理系统，支持多种大模型（如 Ollama、LM Studio 等），提供 Web 界面、搜索功能（集成 SearxNG）、浏览器自动化（ChromeDriver）和任务规划能力。用户可通过配置 `config.ini` 文件选择模型服务地址，安装依赖后运行本地服务或 Docker 容器。项目强调隐私保护，所有模型、搜索和语音处理均本地完成，避免 API 费用。支持大模型（如 70B 参数），但需根据模型规模配置相应硬件（如 48GB 显存）。提供常见故障排查指南，如 ChromeDriver 版本匹配、连接适配器错误处理等。