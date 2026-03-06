
---
title: crocodile
---

### [labulakalia crocodile](https://github.com/labulakalia/crocodile)  ![GitHub Repo stars](https://img.shields.io/github/stars/labulakalia/crocodile?style=social)

Crocodile 是一个基于 Golang 的分布式任务调度系统，支持 Linux、Mac、Windows 平台。系统采用调度中心与 Worker 节点架构，通过 gRPC 通信，依赖 Redis 和 MySQL 进行数据存储。主要功能包括：支持 HTTP 请求及 Golang、Python、Shell 等多种语言的任务远程执行；提供 Web 界面实现任务全生命周期管理（增删改查、克隆、运行、终止）及实时日志查看；支持多种调度算法、主从任务依赖关系及宿主机组绑定策略；具备自定义报警机制，支持任务结果校验及邮件、微信、钉钉等多种通知渠道；提供证书加密、访问令牌、操作审计及多级权限控制等安全功能；支持 Docker Compose 及二进制部署，并可配置多调度中心以实现高可用。