
---
title: AP2
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/google-agentic-commerce/AP2?style=social) ](https://github.com/google-agentic-commerce/AP2)
### [google-agentic-commerce AP2](https://github.com/google-agentic-commerce/AP2)

**项目核心内容总结：**

1. **项目功能**  
   Agent Payments Protocol (AP2) 是一个代理支付协议的实现，提供代码示例和演示，用于展示协议的关键组件。支持通过 Android 或 Python 实现多种支付场景，核心功能包括代理间支付流程的自动化处理。

2. **使用方法**  
   - **环境准备**：需 Python 3.10+ 和 `uv` 包管理器。  
   - **认证方式**：可选 Google API Key（开发推荐）或 Vertex AI（生产推荐），通过环境变量或 `.env` 文件配置。  
   - **运行场景**：进入项目根目录，执行 `run.sh` 脚本安装依赖并启动代理，通过购物代理的 URL 进行交互。  
   - **类型包安装**：通过 `uv pip install` 命令直接安装 GitHub 上的 `ap2/types` 模块。

3. **主要特性**  
   - **灵活性**：不强制依赖 ADK 或 Gemini 2.5 Flash，支持自定义工具。  
   - **多平台示例**：提供 Android 和 Python 的场景示例，代码分别位于 `samples/android` 和 `samples/python/src`。  
   - **模块化设计**：协议核心对象定义在 `src/ap2/types`，便于扩展和集成。