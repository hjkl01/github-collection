
---
title: crocodile
---

### [labulakalia crocodile](https://github.com/labulakalia/crocodile)  ![GitHub Repo stars](https://img.shields.io/github/stars/labulakalia/crocodile?style=social)

Crocodile 是一款基于 Golang 的分布式任务调度系统，支持 Web 界面进行任务管理（增删改查克隆），提供实时日志监控与任务终止功能。系统支持 HTTP 请求及 Golang、Python、Shell、Nodejs、Bat 等多种脚本执行，提供随机、轮询、权重等调度算法，支持父子任务关联与串行/并行执行策略。具备完善的告警通知功能，支持邮件、微信、钉钉等多种渠道，并可自定义任务成功判定标准。系统采用调度中心与 Worker 节点架构，支持宿主机分组与动态发现，利用 Redis 和 MySQL 存储，提供证书加密通信、访问令牌、多角色权限控制及操作审计等安全机制，兼容 Linux、Mac、Windows 平台。