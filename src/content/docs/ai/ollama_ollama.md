
---
title: ollama
---

### [ollama ollama](https://github.com/ollama/ollama)

**项目核心内容总结：**

1. **功能**  
   - Ollama 是一个本地运行的大型语言模型（LLM）服务，支持多种模型（如 Llama、Mistral 等），提供 API 接口用于运行、管理和部署模型，适用于代码生成、对话、数据分析等场景。  
   - 支持跨平台（Windows、Linux、macOS）及多语言（Python、JavaScript 等）集成。  

2. **使用方法**  
   - 安装 Ollama 后，通过命令行加载模型并启动服务；  
   - 通过 HTTP API 调用模型进行推理，支持自定义参数（如温度、最大长度）；  
   - 可集成到应用、插件（如 Obsidian、Discord、Telegram 等）或开发工具（如 VS Code、Qt Creator）。  

3. **主要特性**  
   - **本地化部署**：无需依赖云端，数据隐私更高；  
   - **模型兼容性**：支持 llama.cpp 等多种模型格式；  
   - **社区生态**：提供大量插件（如代码助手、聊天机器人）、扩展（如 KDE 控制面板）和部署方案（如 AWS 自动化部署）；  
   - **可观察性工具**：集成 Opik、Lunary 等平台，支持模型监控、调试和性能分析；  
   - **安全增强**：通过 Ollama Fortress 代理服务器实现访问控制与防护。  

4. **支持后端**  
   - 依赖 llama.cpp 项目（由 Georgi Gerganov 开发），支持 GPU 加速推理。  

5. **其他工具**  
   - 提供安全代理（Ollama Fortress）、本地 AI 助手（如 NativeMind）、开发插件（如 QodeAssist）及自动化部署方案（如 Terraform 模块）。