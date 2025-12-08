
---
title: droidrun
---

### [droidrun droidrun](https://github.com/droidrun/droidrun)

**项目核心内容总结：**

**项目功能**  
DroidRun 是一个通过大型语言模型（LLM）代理控制 Android 和 iOS 设备的框架，支持用自然语言命令自动化设备交互，适用于移动应用测试、任务自动化等场景。

**主要特性**  
- 支持多平台（Android/iOS）及多 LLM 服务商（OpenAI、Anthropic、Gemini 等）  
- 支持复杂多步骤任务规划、CLI 工具调试、Python API 扩展开发  
- 提供截图分析、执行追踪（Arize Phoenix）等功能  

**使用方法**  
1. 安装：`pip install 'droidrun[google,anthropic,openai,deepseek,ollama,dev]'`  
2. 参考文档快速入门（[链接](https://docs.droidrun.ai/v3/quickstart)）  
3. 查看演示视频（如住宿预订、趋势追踪、 streak 保存等场景）  

**其他**  
- 提供中文等多语言文档  
- 开源 MIT 许可证，集成安全检查工具（bandit、safety）