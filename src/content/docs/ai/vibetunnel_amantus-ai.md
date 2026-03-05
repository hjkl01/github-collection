
---
title: vibetunnel
---

### [amantus-ai vibetunnel](https://github.com/amantus-ai/vibetunnel)  ![GitHub Repo stars](https://img.shields.io/github/stars/amantus-ai/vibetunnel?style=social)

VibeTunnel 是一款将本地终端会话代理至浏览器中的应用，允许用户通过任何设备的浏览器远程访问和控制本地终端，无需复杂的 SSH 配置。

**核心功能：**
1. **跨平台终端代理**：提供 macOS 原生应用（Apple Silicon 优化）和 npm 包（支持 Linux/Headless 系统），将终端输出实时同步至 Web 界面。
2. **安全远程连接**：支持通过 Tailscale（私有/公共模式）或 ngrok 建立加密隧道，实现安全的远程监控与协作。
3. **开发者工具增强**：包含 Git 跟随模式（自动同步工作区分支）、终端标题管理、会话录制及 Shell 别名自动解析。
4. **灵活安全认证**：支持系统认证、SSH 密钥、环境变量等多种模式，适配本地开发至生产环境部署。