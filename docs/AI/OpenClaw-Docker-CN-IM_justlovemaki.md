### [justlovemaki OpenClaw-Docker-CN-IM](https://github.com/justlovemaki/OpenClaw-Docker-CN-IM)  ![GitHub Repo stars](https://img.shields.io/github/stars/justlovemaki/OpenClaw-Docker-CN-IM?style=social)

该项目是一个基于 Docker 的 AI 机器人网关镜像，专为集成中国主流即时通讯平台（IM）而设计。其核心功能包括：

- **预装主流 IM 平台插件**：支持飞书（含官方团队插件）、钉钉、QQ 机器人、企业微信等。
- **Docker 快速部署**：通过环境变量灵活配置各平台凭证，一键启动。
- **AI 模型集成**：支持 OpenAI 和 Claude 协议的 AI 模型，推荐搭配 AIClient-2-API 实现无限 Token 调用。
- **内置工具**：集成 OpenCode AI 代码助手、Playwright 浏览器自动化工具和中文 TTS 语音合成。
- **数据持久化**：支持配置和工作空间数据的持久化存储。
- **多账号支持**：支持企业微信等平台的多机器人账号配置。
- **高级功能**：提供官方飞书插件的完整 OAPI 能力，如日历、任务、多维表格等。

该项目适用于需要快速部署多平台 AI 机器人网关的场景，尤其适合与 AIClient-2-API 配合使用以降低 Token 消耗成本。