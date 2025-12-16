
---
title: adk-python
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/google/adk-python?style=social) ](https://github.com/google/adk-python)
### [google adk-python](https://github.com/google/adk-python)

**Agent Development Kit (ADK) 核心内容总结：**

**项目功能**  
ADK 是一个开源的 Python 框架，用于构建、评估和部署 AI 代理（Agent），支持从简单任务到复杂系统的开发。兼容多种模型和部署方式（如 Cloud Run、Vertex AI），并优化适配 Gemini。

**主要特性**  
- **代码优先开发**：通过 Python 直接定义代理逻辑、工具和协作流程，支持灵活扩展和版本控制。  
- **多代理系统**：支持模块化设计，可组合多个专业化代理形成层级结构。  
- **工具生态**：集成预置工具、自定义函数、OpenAPI 接口等，支持与 Google 生态无缝对接。  
- **部署灵活**：支持容器化部署及规模化扩展。  
- **交互增强**：提供工具确认流程（HITL）、会话回退（Rewind）等功能。  

**使用方法**  
- **安装**：  
  - 稳定版：`pip install google-adk`  
  - 开发版：`pip install git+https://github.com/google/adk-python.git@main`  
- **示例**：  
  - 单代理定义：通过 `Agent` 类配置模型、工具和指令。  
  - 多代理系统：通过 `sub_agents` 参数组合多个代理，由协调器代理统一管理任务。  

**其他**  
- 提供内置开发 UI 用于测试和调试代理。  
- 支持通过 `adk eval` 命令评估代理性能。  
- 项目采用 Apache 2.0 协议开源。