### [DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) ![GitHub Repo stars](https://img.shields.io/github/stars/Hmbown/DeepSeek-TUI?style=social)

DeepSeek TUI 是一个在终端运行的 AI 编码代理（命令为 `deepseek`），基于 DeepSeek V4，支持流式推理展示与 100 万 token 上下文。

核心功能包括：读取/编辑本地文件、执行 Shell、Git 操作、网页搜索浏览、补丁应用、子代理协作、MCP 工具扩展、LSP 诊断反馈、会话保存恢复、工作区快照回滚、持久任务队列、实时 token/费用统计与缓存命中分析。

它提供三种工作模式：Plan（只读规划）、Agent（审批后执行）、YOLO（自动审批）；并支持 Auto 模式按每轮任务自动选择模型（`deepseek-v4-flash`/`deepseek-v4-pro`）和思考强度（off/high/max），兼顾效果与成本。

项目还支持 HTTP/SSE 无头服务接口（`deepseek serve --http`）、ACP 适配、技能系统（可从 GitHub 安装指令包）、多语言界面、本地与项目级配置、以及多供应商/自托管兼容（如 OpenAI 兼容端点、NVIDIA NIM、Fireworks、SGLang、vLLM、Ollama）。