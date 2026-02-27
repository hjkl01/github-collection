
---
title: nanobot
---

### [HKUDS nanobot](https://github.com/HKUDS/nanobot)  ![GitHub Repo stars](https://img.shields.io/github/stars/HKUDS/nanobot?style=social)

# nanobot：超轻量级个人 AI 助手

### 项目简介
nanobot 是一款灵感源自 OpenClaw 的超轻量级个人 AI 代理助手。其核心代理代码仅约 4,000 行，比 Clawdbot 小 99%，具有启动快、资源占用低、代码清晰易读等特点，非常适合个人使用及研究扩展。

### 核心特性
*   **多模型支持**：支持 OpenRouter、Anthropic、OpenAI、DeepSeek、Gemini、VolcEngine 等主流 LLM 提供商；支持本地 vLLM 部署及自定义 OpenAI 兼容接口；支持 OAuth 登录（如 OpenAI Codex）。
*   **多平台集成**：内置集成 Telegram、Discord、WhatsApp、Feishu（飞书）、DingTalk（钉钉）、Slack、Email、QQ、Mochat、Matrix 等聊天渠道。
*   **高级功能**：支持 MCP（模型上下文协议）扩展外部工具，内置记忆系统、定时任务（Cron）、心跳机制（定期任务执行）及子代理功能。
*   **部署灵活**：支持命令行交互、Docker 容器化部署及 Linux Systemd 用户服务。

### 使用方法
1.  **安装**：
    *   源码安装（推荐开发）：`git clone https://github.com/HKUDS/nanobot.git` 并 `pip install -e .`
    *   工具安装：`uv tool install nanobot-ai`
    *   标准安装：`pip install nanobot-ai`
2.  **初始化与配置**：
    *   运行 `nanobot onboard` 初始化配置及工作区。
    *   编辑 `~/.nanobot/config.json`，填入 API 密钥（如 OpenRouter）并配置默认模型。
3.  **运行**：
    *   交互模式：`nanobot agent`（直接对话）。
    *   网关模式：`nanobot gateway`（连接聊天应用，需先配置渠道）。

### 配置与安全
*   **提供商**：通过 `nanobot/providers/registry.py` 注册新 Provider，仅需两步即可支持新模型。
*   **安全**：生产环境可设置 `restrictToWorkspace` 限制工具访问范围，支持 `allowFrom` 设置用户白名单。
*   **Docker**：使用 `-v` 参数挂载配置目录以持久化数据。
*   **扩展**：支持 Agent 社交网络（Moltbook, ClawdChat）及自定义技能。
