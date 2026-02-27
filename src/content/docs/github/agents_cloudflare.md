
---
title: agents
---

### [cloudflare agents](https://github.com/cloudflare/agents)  ![GitHub Repo stars](https://img.shields.io/github/stars/cloudflare/agents?style=social)

**项目名称**：Cloudflare Agents

**项目简介**：  
Cloudflare Agents 是一个基于 [Cloudflare Durable Objects](https://developers.cloudflare.com/durable-objects/) 构建的持久、有状态的执行环境，专为代理工作负载（agentic workloads）设计。每个代理（Agent）拥有独立的状态、存储和生命周期，支持实时通信、调度、AI模型调用、MCP、工作流等功能。当代理空闲时会休眠，按需唤醒，可高效运行数百万个实例，如每个用户、会话或游戏房间一个代理，且在非活跃状态下无成本。

---

**使用方法**：  
- 创建新项目：

  ```
  npm create cloudflare@latest -- --template cloudflare/agents-starter
  ```

- 添加到已有项目：

  ```
  npm install agents
  ```

---

**主要功能与特性**：

| 功能 | 描述 |
|------|------|
| **持久状态** | 状态同步所有连接客户端，支持重启后恢复 |
| **可调用方法** | 使用 `@callable()` 装饰器实现类型安全的远程过程调用（RPC） |
| **调度任务** | 支持一次性、重复性、基于 cron 的任务 |
| **WebSocket** | 实现实时双向通信，支持生命周期钩子 |
| **AI 聊天** | 持久消息、可恢复流式传输、服务端/客户端工具执行 |
| **MCP** | 可作为 MCP 服务器或客户端 |
| **工作流** | 支持多步骤任务，含人工审批 |
| **电子邮件** | 通过 Cloudflare 邮件路由接收和响应邮件 |
| **代码模式（Code Mode）** | LLM 生成可执行的 TypeScript 代码 |
| **SQL** | 通过 Durable Objects 直接执行 SQLite 查询 |
| **React 集成** | 提供 `useAgent` 和 `useAgentChat` 钩子用于前端集成 |
| **纯 JS 客户端** | `AgentClient` 用于非 React 环境 |

**即将支持**：实时语音代理、网页浏览（无头浏览器）、沙箱代码执行、多通道通信（短信、消息应用）。

---

**相关包**：

| 包名 | 描述 |
|------|------|
| `agents` | 核心 SDK，含代理类、路由、状态、调度、MCP、邮件、工作流等 |
| `@cloudflare/ai-chat` | 高级 AI 聊天功能 |
| `hono-agents` | Hono 框架的代理中间件 |
| `@cloudflare/codemode` | 实验性：LLM 生成可执行代码 |

---

**示例与文档**：

- 示例项目位于 `examples/` 目录，涵盖 MCP、工作流、邮件代理等
- 提供 OpenAI Agents SDK 示例
- 完整文档：[Cloudflare 开发者文档](https://developers.cloudflare.com/agents/)
- 本地运行示例：

  ```
  cd examples/playground
  npm run dev
  ```

---

**开发信息**：

- 要求 Node.js 24+
- 使用 npm 工作区
- 构建、测试、格式化等命令：

  ```
  npm install
  npm run build
  npm run check
  CI=true npm test
  ```

- 包更新需使用 `changeset` 生成变更记录

---

**贡献方式**：

- 目前不接受外部 PR，但欢迎：
  - [提交问题或功能建议](https://github.com/cloudflare/agents/issues)
  - [参与讨论](https://github.com/cloudflare/agents/discussions)

---

**许可证**：MIT