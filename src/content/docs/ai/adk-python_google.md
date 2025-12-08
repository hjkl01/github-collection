
---
title: adk-python
---

### [google adk-python](https://github.com/google/adk-python)

**项目核心内容总结：**  

**项目功能**：  
Agent Development Kit (ADK) 是一个开源的 Python 框架，用于构建、评估和部署复杂的 AI 代理系统，支持从简单任务到复杂系统的灵活开发，兼容多种模型和部署环境（如 Gemini、Vertex AI 等）。  

**使用方法**：  
- **安装方式**：  
  - 稳定版：`pip install google-adk`  
  - 开发版：`pip install git+https://github.com/google/adk-python.git@main`  
- **功能示例**：  
  - 定义单代理：通过代码配置代理名称、模型、指令及工具（如 Google 搜索）。  
  - 定义多代理系统：通过层级结构组合多个代理（如协调器、执行器）。  
- **评估命令**：使用 `adk eval` 命令对代理进行测试。  

**主要特性**：  
1. **工具生态**：集成预置工具、自定义函数、OpenAPI 等，支持与 Google 生态深度结合。  
2. **代码优先开发**：所有逻辑和工具通过 Python 定义，支持灵活开发、测试和版本控制。  
3. **无代码配置**：支持通过配置文件构建代理（Agent Config）。  
4. **工具确认流程**：提供人工确认（HITL）机制，确保关键操作安全。  
5. **模块化多代理**：支持构建多代理协作系统，适用于复杂场景。  
6. **灵活部署**：支持容器化部署（如 Cloud Run）及 Vertex AI 扩展。  
7. **新功能**：支持自定义服务注册、会话回退（Rewind）、代码执行沙盒（CodeExecutor）等。  

**其他**：  
- 提供内置开发 UI 用于测试和调试代理。  
- 文档和示例代码可通过官方链接获取。