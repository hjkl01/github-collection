
---
title: openclaw
---

### [openclaw openclaw](https://github.com/openclaw/openclaw)  ![GitHub Repo stars](https://img.shields.io/github/stars/openclaw/openclaw?style=social)

OpenClaw 是一个**个人 AI 助手**，可以在本地设备上运行，支持通过多种通信渠道（如 WhatsApp、Telegram、Slack、Discord、Google Chat、Signal、iMessage、Microsoft Teams、WebChat 等）进行交互。它可以执行语音识别、文本生成、浏览器控制、设备操作（如摄像头、屏幕录制）、执行命令、定时任务、Webhook 触发等操作。

### 核心功能
1. **多平台支持**：支持多种消息平台和设备，包括 iOS、Android、macOS。
2. **语音与文本交互**：支持语音唤醒、语音交互，以及基于文本的聊天。
3. **本地控制面板**：通过 Gateway（网关）控制所有会话、通道和工具。
4. **模型支持**：支持多种大语言模型，如 Anthropic、OpenAI，并提供模型切换与故障转移机制。
5. **安全机制**：支持私聊限制、身份验证、权限控制，确保数据安全。
6. **开发与部署**：支持通过 Nix、Docker 等方式部署，提供开发环境与调试工具。

### 使用方法
1. **安装**：使用 npm、pnpm 或 bun 安装 OpenClaw，并运行 `openclaw onboard` 进行设置。
2. **配置**：通过配置文件设置模型、通道、权限等参数。
3. **运行**：启动网关服务后，即可通过命令行或客户端与 AI 助手进行交互。

### 主要特性
- **多通道集成**：支持多种消息平台的实时交互。
- **本地控制**：所有数据和处理均在本地完成，确保隐私。
- **扩展性强**：支持自定义技能、插件、工具和自动化任务。
- **安全与权限管理**：提供详细的权限控制和安全策略，防止未授权访问。
- **跨平台支持**：支持 Windows（通过 WSL2）、Linux、macOS。

### 适用场景
- 个人助理：管理日常任务、提醒、信息查询等。
- 家庭自动化：控制智能家居设备、执行定时任务。
- 本地 AI 交互：提供本地化的 AI 助手体验，无需依赖云端服务。