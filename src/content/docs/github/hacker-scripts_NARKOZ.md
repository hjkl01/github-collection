
---
title: hacker-scripts
---

### [NARKOZ hacker-scripts](https://github.com/NARKOZ/hacker-scripts)  ![GitHub Repo stars](https://img.shields.io/github/stars/NARKOZ/hacker-scripts?style=social)

该项目提供了一系列基于真实故事的命令行脚本，用于实现自动化操作及恶作剧功能：

1. `smack-my-bitch-up.sh`：晚 9 点后检测 SSH 活跃会话，自动向配偶发送加班短信。
2. `kumar-asshole.sh`：扫描邮件关键词，触发后远程回滚客户数据库并回复安抚邮件。
3. `hangover.sh`：早 8:45 无交互式会话时，自动发送请假或居家办公邮件。
4. `fucking-coffee.sh`：定时通过 Telnet 向联网咖啡机发送指令以模拟冲煮流程。

项目需配置 Twilio 和 Gmail 环境变量，支持通过 Cron 进行定时任务调度，采用 WTFPL 协议发布。