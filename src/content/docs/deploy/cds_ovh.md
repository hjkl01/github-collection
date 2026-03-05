
---
title: cds
---

### [ovh cds](https://github.com/ovh/cds)  ![GitHub Repo stars](https://img.shields.io/github/stars/ovh/cds?style=social)

CDS 是一个基于 Go 语言开发的企业级持续交付与 DevOps 自动化平台，核心功能如下：

1. **工作流编排**：提供 Web UI 和命令行工具（cdsctl），支持构建复杂工作流、管道链式调用及模板复用。
2. **Git 集成**：支持工作流即代码，与 GitHub/GitLab 等主流版本控制系统双向集成，支持多分支策略与自动化触发。
3. **执行环境**：支持作业隔离与并发执行，可启动临时服务（如数据库），支持制品传输及多语言、多平台兼容性。
4. **架构扩展**：API 无状态设计支持高可用与水平扩展，支持多云按需自动扩容（Kubernetes/OpenStack 等），提供 REST API、SDK 及自定义插件。
5. **企业级特性**：实现多租户隔离、细粒度权限控制、多环境管理、内置监控指标及消息通知功能。