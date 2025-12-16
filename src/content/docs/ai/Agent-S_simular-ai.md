
---
title: Agent-S
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/simular-ai/Agent-S?style=social) ](https://github.com/simular-ai/Agent-S)
### [simular-ai Agent-S](https://github.com/simular-ai/Agent-S)

**项目核心内容总结：**  
Agent S3 是一个让 AI 像人类一样操作电脑的智能代理框架，支持通过自然语言指令执行关闭软件、文件处理、系统配置等任务。  

**使用方法：**  
1. **命令行工具**：通过 CLI 部署，需配置主生成模型（如 GPT-5）和定位模型（如 UI-TARS 系列）的参数，包括模型地址、分辨率、API 密钥等。  
2. **SDK 集成**：提供 Python 接口，导入 `AgentS3` 和 `OSWorldACI` 类，通过设置引擎参数、定位模型维度（如 1920x1080）及启用本地代码执行环境（可选）实现功能。  

**主要特性：**  
- **多模型兼容**：支持主流生成模型（如 OpenAI、Anthropic）和高精度定位模型（如 UI-TARS-1.5B/72B）。  
- **本地代码执行**：可运行 Python/Bash 代码处理数据、文件或系统任务（需注意安全风险）。  
- **反射代理辅助**：通过反思机制优化任务执行逻辑。  
- **部署灵活**：支持 OSWorld 等平台部署，适应不同场景需求。