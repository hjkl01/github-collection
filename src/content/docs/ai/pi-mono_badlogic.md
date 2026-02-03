
---
title: pi-mono
---

### [badlogic pi-mono](https://github.com/badlogic/pi-mono)  ![GitHub Repo stars](https://img.shields.io/github/stars/badlogic/pi-mono?style=social)

该项目是一个名为 Pi 的多功能 AI 代理工具集，主要用于构建 AI 代理和管理大型语言模型（LLM）的部署。项目采用多包架构（monorepo），包含多个功能模块：

### 项目功能与主要特性：
- **pi-coding-agent（编码代理）**：提供交互式编码代理的命令行界面，是项目的核心工具之一。
- **pi-ai**：支持多种 LLM 提供商（如 OpenAI、Anthropic、Google 等）的统一 API。
- **pi-agent-core**：代理运行时，支持工具调用和状态管理。
- **pi-mom**：Slack 机器人，可将消息委派给 pi 编码代理处理。
- **pi-tui**：终端 UI 库，支持差异渲染。
- **pi-web-ui**：用于 AI 聊天界面的网页组件。
- **pi-pods**：用于在 GPU 集群上管理 vLLM 部署的命令行工具。

### 使用方法：
1. 安装依赖：`npm install`
2. 构建所有包：`npm run build`
3. 检查代码：`npm run check`
4. 运行测试：`./test.sh`（如无 API 密钥，将跳过依赖 LLM 的测试）
5. 从源码运行 pi：`./pi-test.sh`（需在项目根目录运行）

### 开发与贡献：
- 贡献指南详见 `CONTRIBUTING.md`
- 项目特定规则详见 `AGENTS.md`

### 许可：
- MIT 开源协议