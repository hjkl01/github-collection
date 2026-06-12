### [9router](https://github.com/decolua/9router) ![GitHub Repo stars](https://img.shields.io/github/stars/decolua/9router?style=social)

9Router 是一个免费的本地 AI 路由器，面向 Claude Code、Cursor、Codex、OpenClaw、Cline 等编程工具，提供统一的 OpenAI 兼容接口，将请求智能分发到 40+ 提供商和 100+ 模型。

核心功能：
- **RTK Token Saver**：自动压缩 `tool_result`（如 git diff、grep、ls 等）内容，每次请求可节省约 **20–40% 输入 token**。
- **Caveman 模式**：压缩输出表达，在保留技术信息下可进一步减少输出 token。
- **三层自动降级路由**：**订阅模型 → 低价模型 → 免费模型**，在额度用尽或报错时自动切换，尽量不断线。
- **实时额度与用量跟踪**：监控 token、重置时间、成本趋势，提升订阅利用率。
- **格式转换与广泛兼容**：支持 OpenAI / Claude / Gemini / Cursor / Kiro / Vertex 等格式互转。
- **多账号轮询与自动刷新 OAuth Token**：提升稳定性与可用性。
- **自定义模型组合（Combos）**：可配置多级 fallback 策略。
- **请求日志、云同步、可视化面板**：便于调试、跨设备同步与运维。
- **多部署方式**：本地、VPS、Docker、Cloudflare Workers。

项目定位：以“不断线编码 + 降低成本”为目标，通过免费与低价模型路由及 token 优化，帮助开发者在高强度编码场景中持续可用并减少开销。
