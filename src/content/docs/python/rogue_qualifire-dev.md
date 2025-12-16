
---
title: rogue
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/qualifire-dev/rogue?style=social) ](https://github.com/qualifire-dev/rogue)
### [qualifire-dev rogue](https://github.com/qualifire-dev/rogue)

**项目核心内容总结：**

**功能：**  
Rogue 是一个用于评估 AI 代理（如聊天机器人）性能、合规性和安全性的工具，支持通过预设场景测试代理的政策遵循能力，并生成评估报告。支持多种模型（如 OpenAI、Gemini、Anthropic）和协议（A2A、MCP）。

**使用方法：**  
1. **安装**：通过 `uv sync` 或 `pip install` 安装依赖。  
2. **运行模式**：  
   - **TUI/WebUI 模式**：通过命令 `uvx rogue-ai` 启动，配置代理地址、LLM 模型等参数，实时观察测试过程。  
   - **CLI 模式**：非交互式自动化测试，需指定代理地址、场景文件、LLM 模型、业务背景等参数，适合 CI/CD 流程。  
3. **配置文件**：支持通过 JSON 文件配置参数，覆盖 CLI 参数默认值。

**主要特性：**  
- 动态生成测试场景：基于用户提供的业务背景自动生成测试用例。  
- 实时交互监控：TUI/WebUI 中可观看评估代理与目标代理的对话过程。  
- 详细报告生成：评估结束后生成 Markdown 格式报告，包含通过率、问题分析和建议。  
- 多协议兼容：支持 A2A（基于 HTTP 的代理协议）和 MCP（基于消息的代理协议）。  
- 自动化测试：CLI 模式适合集成到自动化测试流程中。

**许可证：**  
项目开源，禁止商业销售。如需商业使用，需联系 `admin@qualifire.ai`。