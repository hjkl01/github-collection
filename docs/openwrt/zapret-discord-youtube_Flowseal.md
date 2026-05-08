### [zapret-discord-youtube](https://github.com/Flowseal/zapret-discord-youtube) ![GitHub Repo stars](https://img.shields.io/github/stars/Flowseal/zapret-discord-youtube?style=social)

该项目是基于 zapret 的 Windows 一键配置包，主要用于通过多种可切换策略（如 ALT、FAKE 等）进行网络流量绕过，解决 Discord、YouTube、Telegram Web 等服务在部分网络环境下不可用或连接异常的问题。

核心功能包括：
- 提供 `general.bat` 手动启动不同绕过策略，便于逐个测试可用性；
- 提供 `service.bat` 进行服务化管理：安装/移除开机自启、状态检查、自动更新检查、策略测试与常见故障诊断；
- 支持更新 `ipset-all.txt` 与 hosts（用于修复 Telegram 网页版和 Discord 语音连接问题）；
- 支持游戏流量过滤模式与 IPSet 过滤模式开关；
- 支持自定义域名/IP 的包含与排除列表，扩展需要绕过的资源范围。

项目依赖 WinDivert 进行流量拦截与过滤（可能被杀毒软件标记为风险工具但并非病毒），并强调需先配置 Secure DNS 才能提升 YouTube/Discord 等服务的成功率。整体定位是面向 Windows 用户的 zapret 策略管理与故障排查工具集。