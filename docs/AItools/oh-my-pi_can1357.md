### [oh-my-pi](https://github.com/can1357/oh-my-pi) ![GitHub Repo stars](https://img.shields.io/github/stars/can1357/oh-my-pi?style=social)

这是一个面向真实开发场景的终端优先编程智能体平台，基于 Pi 分叉并增强，提供开箱即用的完整编码工作流。项目支持 40+ 模型/提供商、32 个内置工具、LSP 与 DAP 深度集成，可在 macOS、Linux、Windows 上原生运行，并提供 CLI、TUI、Node SDK、RPC、ACP 多种接入方式。

核心功能包括：统一的文件读取、搜索、写入与结构化 AST 编辑；基于内容哈希的高可靠补丁编辑；代码执行与工具联动，支持持久化 Python 和 JavaScript/Bun 运行环境；IDE 级代码智能，支持诊断、跳转、重命名、代码操作；真实调试器接入，支持 LLDB、Delve、debugpy 等；并行子智能体协作与任务拆分；代码评审、PR/Issue 读取、GitHub 统一文件系统式访问；跨会话项目记忆；浏览器与网页搜索；合并冲突解析；预览后确认应用修改；以及规则注入、上下文回退、检查点等高级会话控制能力。

项目强调“内建而非外挂”的工具体系：支持文件、目录、压缩包、SQLite、PDF、网页、内部协议路径等统一读写；支持 bash、任务执行、SSH、图片生成与识别、Mermaid 渲染、计算、后台作业管理等；还可继承 Cursor、Cline、Codex、Copilot 等已有规则与配置，无需迁移。

底层以约 2.7 万行 Rust 原生实现高性能能力，将搜索、Shell、AST、语法高亮、PTY、文本处理、图片编解码、Token 统计等能力以内嵌方式提供，减少外部依赖与进程开销。整体目标是提供一个可扩展、可配置、适合长期使用且不易“用到上限”的编码智能体平台。