
---
title: openfang
---

### [RightNow-AI openfang](https://github.com/RightNow-AI/openfang)  ![GitHub Repo stars](https://img.shields.io/github/stars/RightNow-AI/openfang?style=social)

OpenFang 是一个基于 Rust 的开源智能体操作系统，旨在构建能够自主全天候工作的独立代理，而非被动响应的聊天框架。其主要功能包括：

1. **自主能力包 (Hands)**：内置 7 种预构建代理能力（如研究、线索挖掘、浏览器自动化等），可独立按日程运行，无需人工持续提示。
2. **极简部署**：编译为单一约 32MB 的二进制文件，无需 Docker 或 Python 环境，支持一键安装与启动。
3. **高安全架构**：提供 16 层安全防御，包含 WASM 沙箱隔离、Merkle 审计链追踪、敏感数据内存自动清零及 SSRF 防护。
4. **广泛集成**：支持 40 种消息渠道适配器（如 Telegram、Slack 等），兼容 27 家 LLM 供应商（123+ 模型），并开放 OpenAI 兼容 API。
5. **全栈工具链**：集成 CLI 命令行、Tauri 桌面应用及迁移工具（支持从 OpenClaw 迁移），采用模块化 Rust 架构。

当前版本为 v0.1.0，采用 MIT 协议。