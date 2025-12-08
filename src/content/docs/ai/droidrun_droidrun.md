
---
title: droidrun
---

### [droidrun droidrun](https://github.com/droidrun/droidrun)

**DroidRun 核心内容总结**  

**项目功能**  
DroidRun 是一个通过 LLM 代理控制 Android 和 iOS 设备的框架，支持用自然语言指令自动化设备操作。  

**主要特性**  
- 支持多 LLM 提供商（如 OpenAI、Anthropic、Gemini 等）  
- 支持复杂多步骤任务的规划  
- 提供 CLI 工具（含增强调试功能）和可扩展的 Python API  
- 支持截图分析与 Arize Phoenix 执行追踪  

**使用方法**  
- 安装：`pip install 'droidrun[google,anthropic,openai,deepseek,ollama,dev]'`  
- 快速入门：参考官方文档（[链接](https://docs.droidrun.ai/v3/quickstart)），提供视频教程  
- 示例场景：住宿预订、趋势追踪、语言学习应用打卡等  

**其他**  
- 开源协议：MIT 许可证  
- 安全检查：集成 `bandit` 和 `safety` 工具，用于代码和依赖项漏洞检测