
---
title: agents
---

### [livekit agents](https://github.com/livekit/agents)

**项目核心内容总结：**  
LiveKit Agents 是一个 Python 框架，用于构建实时、多模态（语音/文本）的可编程 AI 代理，支持创建能“听、说、理解”的智能交互系统。  

**主要功能与特性：**  
1. **灵活集成**：支持语音识别（STT）、自然语言处理（LLM）、文本到语音（TTS）等模块，可扩展第三方工具（如 MCP 服务器）。  
2. **多场景支持**：涵盖语音助手、电话客服、视频 avatar、文本交互等场景，提供示例代码（如餐厅预订、Gemini 视觉交互）。  
3. **开发效率工具**：内置任务调度、语义回合检测、热重载开发模式、终端测试模式及生产优化启动方式。  
4. **开源与生态**：兼容 LiveKit 云服务及自托管服务器，集成 WebRTC、SIP 等协议，支持跨平台客户端（iOS/Android/Flutter 等）。  

**使用方法：**  
- 安装：`pip install` 指定依赖。  
- 开发：通过 `python myagent.py dev` 启动热重载服务器，设置 `LIVEKIT_URL` 等环境变量连接服务。  
- 测试：使用 `console` 模式本地验证逻辑，或通过 [Agents Playground](https://agents-playground.livekit.io/) 快速测试。  
- 部署：运行 `python myagent.py start` 启动生产环境。