
---
title: devzat
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/quackduck/devzat?style=social) ](https://github.com/quackduck/devzat)
### [quackduck devzat](https://github.com/quackduck/devzat)

**项目核心内容总结：**  
Devzat 是一个基于 SSH 的实时聊天工具，用户通过 SSH 连接后进入聊天室而非传统终端。支持跨平台（包括手机）访问，提供以下功能：  
- **核心功能**：SSH 连接聊天、房间切换（`cd #room`）、Markdown 格式支持、代码语法高亮、私信（`=<用户> <消息>`）、时区设置、内置游戏（井字棋、猜字游戏）、表情符号替换。  
- **使用方法**：  
  - 直接运行 `ssh devzat.hackclub.com` 或配置 SSH 简化命令（如 `ssh chat`）。  
  - 首次登录时通过 SSH 用户名设置显示名称，后续用 `nick <名称>` 修改。  
  - 防火墙环境下可使用 `ssh devzat.hackclub.com -p 443`。  
- **自托管**：提供快速部署命令（Go 语言编写），支持集成 Slack/Discord/Twitter 及插件扩展。  
- **权限问题**：若遇 `Permission denied`，可切换至 443 端口（无需密钥）或生成 SSH 密钥对。  

**主要特性**：跨平台访问、多房间聊天、代码高亮、游戏互动、支持第三方集成，适合开发者社区交流。