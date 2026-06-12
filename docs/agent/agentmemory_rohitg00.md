### [agentmemory](https://github.com/rohitg00/agentmemory) ![GitHub Repo stars](https://img.shields.io/github/stars/rohitg00/agentmemory?style=social)

agentmemory 是一个面向 AI 编码助手的持久化记忆系统与 MCP/REST 记忆服务器，基于 iii-engine 构建。它可自动记录会话中的提示词、工具调用、结果与错误，并在下次会话开始时注入相关上下文，让助手“记住”项目架构、技术决策与历史修复过程，减少重复说明与 token 消耗。

项目核心功能包括：跨代理共享记忆（支持 Claude Code、Cursor、Gemini CLI、Codex CLI 等任意 MCP/HTTP 客户端）、混合检索（BM25 + 向量 + 知识图谱，RRF 融合）、四层记忆演化（工作/情节/语义/程序性记忆）、自动遗忘与冲突处理、隐私过滤（自动去除密钥等敏感信息）、团队共享与审计追踪、会话回放、实时可视化 Viewer（3113 端口）、以及丰富的 MCP 工具集（记忆检索、保存、图谱查询、治理删除、行动协同等）。

它提供开箱即用的一键启动（`npx @agentmemory/agentmemory`）、本地优先部署（SQLite/本地嵌入、默认自托管、无外部向量数据库依赖）、可扩展的 iii 控制台可观测能力（追踪、日志、状态与函数调试），并通过大量 API 与配置项支持生产级记忆管理。