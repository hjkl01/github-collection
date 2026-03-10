
---
title: hermes-agent
---

### [NousResearch hermes-agent](https://github.com/NousResearch/hermes-agent)  ![GitHub Repo stars](https://img.shields.io/github/stars/NousResearch/hermes-agent?style=social)

Hermes Agent 是一个具备自我提升能力的 AI 代理程序，由 Nous Research 开发。它通过内置的学习循环，能够从经验中创建技能、在使用中不断优化技能，并主动巩固知识。支持在多种环境中运行，如低价 VPS、GPU 集群或无服务器架构。用户可通过 Telegram 等平台与运行在云 VM 上的 Hermes 交互。

主要功能包括：

- 支持多种大型语言模型（如 OpenAI、Kimi、MiniMax 等），并可快速切换；
- 提供完整的终端用户界面（TUI），支持多行编辑、命令自动补全、历史记录、中断重定向等；
- 跨平台消息网关，支持 Telegram、Discord、Slack、WhatsApp、Signal 和 CLI；
- 内置闭环学习机制，包括自主技能创建、技能优化、全文本会话搜索和用户建模；
- 支持定时自动化任务，如每日报告、夜间备份等；
- 支持并行处理，可创建独立子代理处理并行任务；
- 支持多种终端后端部署，包括 Docker、SSH、Daytona、Modal 等；
- 提供研究功能，如轨迹生成、强化学习环境、模型训练数据压缩等。