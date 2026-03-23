### [amantus-ai vibetunnel](https://github.com/amantus-ai/vibetunnel)  ![GitHub Repo stars](https://img.shields.io/github/stars/amantus-ai/vibetunnel?style=social)

VibeTunnel 是一款将浏览器转化为 Mac 终端的工具，通过代理将本地终端会话投射到 Web 界面，实现无摩擦的远程监控与控制。

**核心功能：**
*   **远程访问**：支持本地浏览器访问或通过 Tailscale/ngrok 进行安全远程连接，无需 SSH 密钥或端口转发。
*   **智能命令**：提供 `vt` 包装命令，支持 Shell 别名解析、Git 工作树跟随模式（主仓库自动同步分支）及交互式会话转发。
*   **会话管理**：具备实时活动指示、会话录制（asciinema 格式）、终端标题管理及多设备响应式界面。
*   **安全认证**：支持系统认证、SSH 密钥、环境变量等多种安全模式，适用于生产或开发环境。
*   **平台支持**：macOS 原生应用（需 Apple Silicon M1+）及 npm 包（支持 Linux/无头系统，需 Node.js 22.12+）。

**架构组成：**
由 macOS 菜单栏应用、高性能 Node.js 服务器及 Web 前端（Lit/ghostty-web）三部分构成。