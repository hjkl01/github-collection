
---
title: flyctl
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/superfly/flyctl?style=social) ](https://github.com/superfly/flyctl)
### [superfly flyctl](https://github.com/superfly/flyctl)

**flyctl 核心内容总结**  

**项目功能**  
flyctl 是 fly.io 的命令行工具，用于管理飞地（fly.io）应用，支持登录账户、查看应用列表、监控应用状态等操作。  

**使用方法**  
1. **安装方式**  
   - **Homebrew**（macOS/Linux/WSL）：`brew install flyctl`  
   - **脚本安装**（MacOS/Linux/WSL）：  
     - 最新版本：`curl -L https://fly.io/install.sh | sh`  
     - 预发布版：`curl -L https://fly.io/install.sh | sh -s pre`  
     - 指定版本：`curl -L https://fly.io/install.sh | sh -s 0.0.200`  
   - **Windows**：运行 PowerShell 脚本 `iwr https://fly.io/install.ps1 -useb | iex`  
   - **GitHub**：从 [Releases](https://github.com/superfly/flyctl/releases) 下载对应版本。  

2. **基础操作**  
   - 登录账户：`fly auth login`  
   - 列出应用：`fly apps list`  
   - 查看应用状态：`fly status -a {app-name}`  

**主要特性**  
- 自动读取当前目录的 `fly.toml` 文件中的 `app` 名称（如 `app: banana`），默认操作对应应用，可通过 `-a` 参数覆盖。  
- 支持 `flyctl` 别名为 `fly`，未来将默认使用 `fly` 命令。  
- 每天（东八区时间周一至周四15:00）自动发布新版本，开发者可通过脚本手动触发版本更新。  
- 提供 Windows 构建脚本 `winbuild.ps1`，用于生成帮助文件并构建二进制文件。