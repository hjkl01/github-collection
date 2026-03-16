### [cloudflare agents](https://github.com/cloudflare/agents)  ![GitHub Repo stars](https://img.shields.io/github/stars/cloudflare/agents?style=social)

Cloudflare Agents 是基于 Cloudflare Durable Objects 的持久化、有状态代理执行框架。

核心功能：
- **高效资源利用**：代理空闲休眠、按需唤醒，支持百万级实例且闲置零成本。
- **状态与通信**：每个代理拥有独立状态与存储，支持实时双向通信和多客户端状态同步。
- **丰富能力集**：内置定时调度、AI 模型调用、MCP 协议、工作流编排（含人工审批）、Email 处理、SQLite 查询及 LLM 代码生成模式。
- **开发者工具**：提供 TypeScript SDK，支持类型安全 RPC，兼容 React Hooks 及原生 JS 客户端。