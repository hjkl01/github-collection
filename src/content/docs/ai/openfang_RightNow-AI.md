
---
title: openfang
---

### [RightNow-AI openfang](https://github.com/RightNow-AI/openfang)  ![GitHub Repo stars](https://img.shields.io/github/stars/RightNow-AI/openfang?style=social)

**项目名称**: OpenFang（Agent Operating System）

**核心定位**: 基于 Rust 构建的开源 Agent 操作系统，提供全天候工作的自主 Agent，而非简单的聊天框架或 LLM 包装器。

**主要特性**:
- **Hands 自主能力包**: 内置 7 种预建 Hands（如 Clip 视频剪辑、Lead 线索挖掘、Researcher 深度研究等），可独立运行、按调度自动工作。支持自定义开发并发布至 FangHub。
- **极简部署**: 编译为单个约 32MB 的二进制文件，无外部依赖，一键安装启动。
- **高性能与低资源**: 冷启动时间 <200ms，空闲内存占用仅 40MB，优于主流竞品。
- **深度安全**: 包含 16 层安全防御体系（如 WASM 双计量沙箱、Merkle 哈希链审计、密钥内存自动清除、SSRF 防护等）。
- **广泛集成**: 支持 40 种消息渠道适配器（Telegram、Slack 等）和 27 个 LLM 提供商（涵盖 200+ 模型），提供 OpenAI 兼容 API 及 140+ 管理端点。

**使用方法**:
1.  **安装**: 运行官方安装脚本（macOS/Linux: `curl -fsSL ... | sh`；Windows: PowerShell 脚本）。
2.  **初始化**: 执行 `openfang init` 配置 LLM 提供商及关键设置。
3.  **启动**: 执行 `openfang start` 启动守护进程，本地仪表盘访问 `http://localhost:4200`。
4.  **管理**: 使用 CLI 命令管理 Hands 生命周期（`activate`, `status`, `pause`）及 Agent 交互。
5.  **迁移**: 支持通过 `openfang migrate` 命令从 OpenClaw 迁移现有 Agent、记忆和配置。

**版本与架构**:
- **当前版本**: v0.1.0（首个公开版本，建议生产环境锁定具体 Commit 以防小版本破坏性变更）。
- **技术栈**: Rust 语言，14 个功能模块 Crate，137K+ 代码行数，模块化内核设计。
- **许可协议**: MIT。