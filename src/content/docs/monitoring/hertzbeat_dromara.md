
---
title: hertzbeat
---

### [dromara hertzbeat](https://github.com/dromara/hertzbeat)  ![GitHub Repo stars](https://img.shields.io/github/stars/dromara/hertzbeat?style=social)

Apache HertzBeat 是一款 AI 驱动的下一代开源实时可观测性系统，旨在帮助用户快速实现可观测性需求。

核心功能包括：

- **统一平台**：整合采集、分析、告警与通知，内置 MCP Server 能力及 AI 交互功能。
- **指标与日志**：支持无 Agent 模式，兼容 Prometheus，统一日志收集（OTLP 协议）。
- **自定义监控**：支持通过 YML 模板配置 Http、Jmx、Ssh、Snmp、Jdbc 等多种协议，覆盖数据库、操作系统、中间件、云原生（K8s/Docker）、网络设备及应用服务。
- **告警管理**：统一管理内外告警源，支持灵活阈值规则、分组收敛、静默抑制，支持 Email、微信、钉钉、Slack 等多种通知渠道。
- **高性能架构**：支持多收集器集群横向扩展，实现多网络隔离监测及云边协同。
- **状态页面**：提供强大的状态页面构建能力，实时对外展示服务状态。

支持 Docker、源码、安装包及 Kubernetes Helm 等多种部署方式。