### [Agent-Reach](https://github.com/Panniantong/Agent-Reach) ![GitHub Repo stars](https://img.shields.io/github/stars/Panniantong/Agent-Reach?style=social)

Agent Reach 是一个给 AI Agent 快速接入互联网能力的开源安装与配置工具。它通过一键安装和更新，让能执行命令行的 Agent 直接具备读网页、搜全网、看 YouTube 字幕、读 GitHub 仓库、解析 RSS，以及访问 Twitter/X、Reddit、B 站、小红书、抖音、LinkedIn、微信公众号、微博、V2EX、雪球、小宇宙播客等平台的能力。

它的核心价值是把原本分散且繁琐的平台工具选型、依赖安装、认证配置和环境诊断统一自动化完成，兼容 Claude Code、OpenClaw、Cursor、Windsurf 等各类 Agent。项目本身不包裹实际功能调用，而是作为“脚手架”帮助 Agent 配好上游工具，安装后 Agent 可直接调用对应 CLI、MCP 或开源组件完成搜索、阅读、抓取和转录等任务。

项目特点包括：完全免费、开源可审查、Cookie 和凭据仅本地保存、支持安全模式和 Dry Run、可通过 `agent-reach doctor` 检查各渠道状态、各平台渠道可插拔替换，便于持续维护和扩展。