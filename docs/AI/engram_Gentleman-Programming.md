### [engram](https://github.com/Gentleman-Programming/engram) ![GitHub Repo stars](https://img.shields.io/github/stars/Gentleman-Programming/engram?style=social)

Engram 是一个为 AI 编程代理提供**持久化记忆**的工具：用单个 Go 二进制（零依赖）把记忆存到本地 SQLite（含 FTS5 全文检索）中，让代理在会话结束后也能保留和找回上下文。它支持任意兼容 MCP 的代理（如 Claude Code、OpenCode、Gemini CLI、Codex、VS Code/Copilot、Cursor、Windsurf 等），并提供 CLI、HTTP API、MCP 服务和终端 TUI。

项目核心功能包括：记忆保存/更新/删除、全文搜索与上下文检索、会话生命周期管理、冲突识别与比较、统计与诊断、项目管理，以及 JSON/Obsidian 导入导出。它还支持基于 Git 的跨设备同步（分块压缩、减少冲突），并提供可选的云端复制与共享（本地数据库始终为权威源），含云端配置、同步、升级修复与故障排查流程。

此外，项目提供 Beta 能力用于“记忆冲突显化”：可跨机器同步冲突关系，提供 conflicts CLI/HTTP 审计与扫描，并可结合代理的 LLM 做语义级冲突判断（在已有订阅下可零额外费用）。整体定位是“一个脑子，本地或云端”，以简单部署和代理无关为重点。