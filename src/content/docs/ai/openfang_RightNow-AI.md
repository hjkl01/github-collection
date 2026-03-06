
---
title: openfang
---

### [RightNow-AI openfang](https://github.com/RightNow-AI/openfang)  ![GitHub Repo stars](https://img.shields.io/github/stars/RightNow-AI/openfang?style=social)

OpenFang 是一个基于 Rust 构建的开源代理操作系统，旨在提供可 24/7 自主工作的智能体而非传统聊天机器人。其核心功能包括：

1. **单二进制部署**：编译为约 32MB 的单一文件，安装简便。
2. **自主智能体（Hands）**：内置 7 种预置智能体（剪辑、获客、情报收集、预测、研究、推特管理、浏览器自动化），支持定时执行与独立运行。
3. **深度安全**：集成 16 层安全系统，涵盖 WASM 沙箱、Merkle 审计链、注入扫描、秘密清除等机制。
4. **广泛连接**：支持 40 种通信渠道适配器、27 个 LLM 供应商（123+ 模型），提供 OpenAI 兼容 API 及 140+ 端点。
5. **多端应用**：包含 CLI 管理、Web 仪表盘及 Tauri 2.0 桌面应用，支持从 OpenClaw 迁移。

当前版本为 v0.1.0，架构完整但属早期发布，生产环境建议锁定提交版本。