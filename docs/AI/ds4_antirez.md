### [ds4](https://github.com/antirez/ds4) ![GitHub Repo stars](https://img.shields.io/github/stars/antirez/ds4?style=social)

ds4.c 是一个**专为 DeepSeek V4 Flash 打造的本地原生推理引擎**，定位非常聚焦，不是通用 GGUF 运行器。其核心功能包括：

- 基于 **Metal** 的高性能推理执行（CLI + 服务端），支持长上下文与多轮对话。
- 仅支持本项目提供的 DeepSeek V4 Flash 专用 GGUF（含特制 2-bit/4-bit 量化），可在高内存 Mac（如 128GB）本地运行。
- 提供 OpenAI/Anthropic 兼容 HTTP API（chat/completions/messages）、SSE 流式输出、工具调用（DSML 与 OpenAI/Anthropic 工具格式互转）。
- 内置“思考模式”控制（thinking / non-thinking / think max）。
- 重点实现 **KV 缓存磁盘化**：将 KV 作为磁盘一级公民，支持跨会话/重启复用前缀，减少重复 prefill，适合超长上下文场景。
- 具备工具调用精确回放与规范化兜底机制，保证无状态客户端多轮对话时与已有 KV 对齐。
- 内置官方向量对齐验证、长上下文测试与调试工具（tokens/logprobs/trace），强调可验证正确性。
- 当前为 **alpha 阶段**；服务端仅支持 Metal，CPU 路径主要用于调试与正确性检查。