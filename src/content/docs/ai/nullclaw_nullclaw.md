
---
title: nullclaw
---

### [nullclaw nullclaw](https://github.com/nullclaw/nullclaw)  ![GitHub Repo stars](https://img.shields.io/github/stars/nullclaw/nullclaw?style=social)

NullClaw 是一个基于 Zig 语言开发的超轻量级全自主 AI 助手基础设施，旨在实现零开销、零妥协的部署体验。

**核心功能与特性：**
1. **极致轻量**：生成 678 KB 静态二进制文件，峰值内存占用约 1 MB，启动时间小于 2 毫秒，可在廉价 ARM 单板或微控制器上运行。
2. **功能完备**：内置 23+ 种 AI 模型提供商、18+ 种通信渠道（Telegram、Discord、Nostr 等）、18+ 种工具集及混合检索（向量+FTS5）记忆系统。
3. **完全模块化**：核心子系统（AI、渠道、工具、内存、运行时、安全等）均通过 vtable 接口设计，支持通过配置无代码替换组件。
4. **安全加固**：默认本地绑定，支持沙盒隔离（Landlock/Docker 等）、敏感信息 ChaCha20 加密、配对认证及严格的访问白名单。
5. **灵活部署**：支持 CLI 交互、网关服务、后台守护进程及边缘 WASM 方案，配置文件兼容 OpenClaw 标准。