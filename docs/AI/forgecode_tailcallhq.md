### [forgecode](https://github.com/tailcallhq/forgecode) ![GitHub Repo stars](https://img.shields.io/github/stars/tailcallhq/forgecode?style=social)

Forge 是一个开源的 AI 增强型终端开发环境与编码代理，核心功能包括：

- 在终端内提供 AI 辅助开发，支持代码理解、功能实现、调试、重构、代码评审、Git 操作与技术学习等场景。
- 提供三种使用模式：交互式 TUI 会话模式、一次性命令行模式（单次 Prompt 执行）、ZSH `:` 前缀插件模式（可直接在 shell 中调用 AI 能力）。
- 内置多代理协作：  
  - `forge`：可改代码并执行实现任务  
  - `sage`：只读分析与问答  
  - `muse`：规划与方案产出（写入 plans/）
- 支持会话管理（新建、切换、克隆、重试、导出、压缩上下文）与文件上下文附加（`@文件`）。
- 深度集成 Git：可基于 diff 自动生成并执行提交，或先预览提交信息。
- 支持自然语言转 shell 命令（suggest）、多行编辑提示词、工具/技能系统与可扩展自定义技能。
- 支持语义检索工作区（代码索引与语义搜索），按语义而非关键词理解代码库。
- 支持多模型与多提供商（如 OpenAI、Anthropic 及 OpenAI 兼容服务），推荐通过 `forge provider login` 进行凭据管理。
- 提供丰富配置能力：`forge.yaml`、环境变量、会话级/全局级模型与推理参数、自定义命令、自定义代理、AGENTS.md 规则注入。
- 支持 MCP（Model Context Protocol）服务接入，可将外部工具与服务纳入 AI 工作流。