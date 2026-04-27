### [pika](https://github.com/dushixiang/pika) ![GitHub Repo stars](https://img.shields.io/github/stars/dushixiang/pika?style=social)

Pika 是一个基于 Go、VictoriaMetrics 与 PostgreSQL/SQLite 的轻量级实时探针监控系统，通过 WebSocket 实现探针与服务端通信，支持数据采集、存储与查询。  
其核心功能包括：系统性能监控（CPU、内存、磁盘、网络、GPU、温度）、服务可用性监控（HTTP/HTTPS、TCP、ICMP/Ping、证书到期）、文件防篡改（实时监控与告警）、安全审计（资产清单、风险分析、历史记录）以及多种认证方式（Basic Auth、OIDC、GitHub OAuth）。  
项目支持 Docker Compose 一键部署，提供 SQLite 和 PostgreSQL 两种部署方案，资源占用低，并具备 Linux 应急响应与安全基线检查能力。