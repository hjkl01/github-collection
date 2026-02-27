
---
title: vibetunnel
---

### [amantus-ai vibetunnel](https://github.com/amantus-ai/vibetunnel)  ![GitHub Repo stars](https://img.shields.io/github/stars/amantus-ai/vibetunnel?style=social)

**VibeTunnel** 是一个将浏览器变成终端工具的项目，允许用户通过浏览器远程访问和操作 Mac 终端。支持 macOS 和 Linux 系统，提供多种远程访问方式（如 Tailscale、ngrok、本地网络等），并具备 AI 代理友好的特性，适合开发和监控 AI 工具。用户可以通过 `vt` 命令在浏览器中运行终端命令，支持 Git 分支自动切换、终端标题管理、安全认证、会话录制等功能。

**核心功能：**
- 通过浏览器访问 Mac 终端，无需 SSH 配置。
- 支持 Tailscale、ngrok 等多种远程访问方式。
- 提供 Git 分支自动切换（Git Follow Mode）。
- 支持终端标题管理，便于多会话区分。
- 提供多种认证方式，如系统认证、SSH 密钥、环境变量等。
- 支持会话录制（asciinema 格式）。
- 提供命令行工具 `vt`，可将终端命令转发到浏览器。
- 支持 macOS 和 Linux，适用于开发、监控、协作等场景。

**使用方法：**
1. **安装**：通过 Homebrew、npm 或直接下载安装。
2. **启动**：运行 VibeTunnel 应用或通过命令行启动服务器。
3. **使用 `vt` 命令**：在终端中运行 `vt [命令]`，即可在浏览器中查看输出。
4. **访问控制面板**：通过 `http://localhost:4020` 查看所有终端会话。

**主要特性：**
- 浏览器访问终端，无需复杂配置。
- 多种认证方式确保安全。
- 支持远程访问，适合移动开发和团队协作。
- Git 分支自动跟随，提升开发效率。
- 会话录制，便于后续回放和分析。
- 支持 macOS 和 Linux，适用于多种开发环境。