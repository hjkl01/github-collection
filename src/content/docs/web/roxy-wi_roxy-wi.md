
---
title: roxy-wi
---

### [roxy-wi roxy-wi](https://github.com/roxy-wi/roxy-wi)

**项目核心内容总结：**

**项目功能**  
Roxy-WI 是一个用于管理 HAProxy、Nginx、Apache 和 Keepalived 的 Web 界面工具，提供配置管理、监控、警报、日志分析、高可用性支持等功能。支持通过 Web 界面动态调整配置（如 Maxconn、黑白名单）、同步多服务器配置、备份配置文件、SSL（含 Let's Encrypt）管理、WAF 防火墙、LDAP 集成等。

**使用方法**  
- **安装方式**：支持 RPM/DEB 包安装（适用于 EL7/8/9、Amazon Linux 2、Ubuntu 等系统）或手动安装。  
- **配置流程**：通过 Web 界面登录（默认账号 admin/admin），添加用户、分组、服务器，并配置相关服务。  
- **错误处理**：若出现“Internal Server Error”，执行 `/var/www/haproxy-wi/app/create_db.py` 初始化数据库。

**主要特性**  
1. 支持动态配置 HAProxy/Nginx，实时生效无需重启服务。  
2. 多服务器配置同步、版本回滚、配置评估功能。  
3. 多用户角色权限管理（如隐藏配置块、分组管理）。  
4. 监控与警报：实时状态查看、连接统计、服务状态通知（Telegram/Slack/邮件等）。  
5. 安全功能：SYN Flood 防护、WAF、SSH 密钥管理、高可用性保障。  
6. 数据库支持：默认 SQLite，可切换为 MySQL。  
7. 集成 SMON 服务，支持网络状态检测（Ping、HTTP、SSL 过期等）。  
8. 移动端适配设计，支持多语言（含中文）。