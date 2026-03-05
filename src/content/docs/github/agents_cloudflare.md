
---
title: agents
---

### [cloudflare agents](https://github.com/cloudflare/agents)  ![GitHub Repo stars](https://img.shields.io/github/stars/cloudflare/agents?style=social)

Cloudflare Agents 是基于 Cloudflare Durable Objects 构建的持久化、有状态的智能体执行环境。每个智能体拥有独立的状态与生命周期，支持闲置休眠、按需唤醒及大规模低成本运行。

主要功能包括：
- **持久化与同步**：状态实时同步客户端，重启保留。
- **RPC 通信**：类型安全的可调用方法。
- **调度与通信**：支持定时任务及 WebSocket 实时双向通信。
- **AI 集成**：支持 AI 聊天（流式传输、工具调用）、MCP 及 Code Mode（LLM 生成代码）。
- **工作流与存储**：支持多步骤任务（含人工审批）、Email 路由及 SQLite 查询。
- **客户端支持**：提供 React Hooks 及原生 JS 客户端。

该项目旨在为每个用户、会话或场景提供独立的智能体环境，内置调度、AI 模型调用及工作流支持。