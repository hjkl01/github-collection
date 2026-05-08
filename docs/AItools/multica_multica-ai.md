### [multica](https://github.com/multica-ai/multica) ![GitHub Repo stars](https://img.shields.io/github/stars/multica-ai/multica?style=social)

Multica 是一个开源的“托管式 AI 编码代理协作平台”，把 Claude Code、Codex、OpenClaw、OpenCode、Hermes、Gemini、Pi、Cursor Agent 等编码代理变成团队成员来管理。你可以像分配同事一样给代理分派 Issue，代理会自主领取任务、执行代码工作、实时汇报进度与阻塞，并在看板和对话中协同。

核心功能包括：代理全生命周期管理（排队/认领/开始/完成/失败）、WebSocket 实时执行监控、可复用技能沉淀（让解决方案在团队内复利）、统一运行时管理（本地 daemon + 云端）、以及多工作区隔离（独立代理、任务与配置）。平台支持云端优先部署，也支持自托管；提供 CLI 完成登录、daemon 启动、工作区与 Issue 管理等操作。

整体架构为 Next.js 前端 + Go 后端（含 WebSocket）+ PostgreSQL（pgvector）+ 本地代理守护进程，面向“人类 + AI 代理”团队在真实项目中的协作开发。