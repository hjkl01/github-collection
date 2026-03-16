### [roxy-wi roxy-wi](https://github.com/roxy-wi/roxy-wi)  ![GitHub Repo stars](https://img.shields.io/github/stars/roxy-wi/roxy-wi?style=social)

Roxy-WI 是一个管理 HAProxy、Nginx、Apache 和 Keepalived 服务器的 Web 图形界面工具，提供友好的操作体验、监控及告警功能。

核心功能：
1. **服务管理**：支持通过 Web 界面安装、更新服务（系统服务或 Docker 方式），管理端口分配及高可用集群配置。
2. **配置维护**：支持动态修改最大连接数、黑白名单及后端信息，一键推送配置至多服务器，支持主从同步、配置备份、历史版本对比与回滚。
3. **监控分析**：提供统一面板查看前后端状态、分析日志及流量指标，支持服务状态及性能异常告警通知（Telegram、Email 等）。
4. **安全控制**：支持多用户角色权限、LDAP、SSL 及 SSH Key 管理，提供 WAF 防护、SYN 洪水保护及配置块隐藏功能。
5. **扩展工具**：内置 SMON 进行网络及服务状态探测，界面适配移动端。