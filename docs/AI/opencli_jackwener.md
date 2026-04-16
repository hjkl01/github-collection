### [opencli](https://github.com/jackwener/opencli) ![GitHub Repo stars](https://img.shields.io/github/stars/jackwener/opencli?style=social)

OpenCLI 是一个统一的自动化命令行平台，可把**网站、浏览器会话、Electron 桌面应用和本地 CLI 工具**转成可复用、可脚本化的确定性命令接口，面向人类与 AI 代理使用。

核心功能：
- 提供三类自动化能力：  
  1) 直接使用内置站点适配器（87+，如 Bilibili、知乎、Reddit、Twitter 等）；  
  2) 用 `opencli browser` 实时控制浏览器（点击、输入、抓取、截图、调试等）；  
  3) 用 `explore/synthesize/generate/cascade` 从真实浏览行为自动生成新适配器并探索认证策略。
- 支持复用 Chrome/Chromium 已登录状态，凭据不离开浏览器，适合需要登录权限的操作。
- 兼容 AI 代理工作流，提供对应 skills（浏览控制、适配器生成、一次性生成等）。
- 作为 CLI Hub 管理本地工具：可统一发现、透传执行并注册外部命令（如 `gh`、`docker` 等）。
- 支持通过 CDP 控制 Electron 应用（如 Cursor、Codex、ChatGPT、Notion、Discord 等）。
- 支持多平台内容下载（图片/视频/文章），并提供 `table/json/yaml/md/csv` 多种输出格式。
- 具备明确退出码、插件扩展机制、CI/脚本友好；运行时零 LLM Token 成本，强调结果可重复与确定性。