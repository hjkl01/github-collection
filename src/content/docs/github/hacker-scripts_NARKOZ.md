
---
title: hacker-scripts
---

### [NARKOZ hacker-scripts](https://github.com/NARKOZ/hacker-scripts)  ![GitHub Repo stars](https://img.shields.io/github/stars/NARKOZ/hacker-scripts?style=social)

该项目是一个基于真实故事的自动化脚本集合，旨在实现特定工作场景的自动操作，主要功能包括：

1. `smack-my-bitch-up.sh`：若晚间 9 点后存在 SSH 活跃会话，自动向指定号码发送加班短信。
2. `kumar-asshole.sh`：扫描指定邮箱中的求助关键词，发现后自动 SSH 连接服务器回滚测试数据库并回复邮件。
3. `hangover.sh`：若早晨 8:45 无活跃会话，自动发送病假或在家办公的邮件。
4. `fucking-coffee.sh`：定时通过 Telnet 控制联网咖啡机制作咖啡。

项目需配置 Twilio 和 Gmail 环境变量，支持通过 Cron 计划任务调度运行，并欢迎提供 Python、Perl 等语言的其他实现。代码遵循 WTFPL 协议。