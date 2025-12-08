
---
title: hacker-scripts
---

### [NARKOZ hacker-scripts](https://github.com/NARKOZ/hacker-scripts)

### 项目核心内容总结

**项目功能**  
该项目包含多个自动化脚本，用于实现幽默或讽刺的自动化操作，例如：  
- `smack-my-bitch-up.sh`：在特定时间通过短信向妻子发送“加班”通知，理由随机生成。  
- `kumar-asshole.sh`：监控邮件，若检测到特定关键词，自动远程回滚数据库并回复邮件。  
- `hangover.sh`：在早晨无交互会话时，发送“生病”等假理由的邮件。  
- `fucking-coffee.sh`：定时通过网络控制咖啡机自动制作咖啡。  

**使用方法**  
1. **环境变量配置**：需设置Twilio短信账户、Gmail邮箱等信息。  
2. **依赖安装**：Ruby脚本需安装`dotenv`、`twilio-ruby`、`gmail`等Gem。  
3. **定时任务**：通过Cron配置脚本执行时间（如每天特定时段运行）。  

**主要特性**  
- 通过脚本实现日常操作自动化，结合幽默场景。  
- 支持定时任务、邮件监控、网络设备控制等功能。  
- 代码开源，采用WTFPL许可证（无限制开源协议）。