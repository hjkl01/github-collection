
---
title: Zappa
---

### [zappa Zappa](https://github.com/zappa/Zappa)  ![GitHub Repo stars](https://img.shields.io/github/stars/zappa/Zappa?style=social)

Zappa 是一个用于在 AWS Lambda 和 API Gateway 上部署无服务器 Python 应用程序的框架，支持 Flask、Django 等 WSGI 应用，实现一键部署、无限扩展、零停机、零维护及按量付费。

核心功能包括：
1. **快速部署与管理**：支持多环境（dev/staging/prod）配置、一键部署、更新、回滚、状态监控、日志查看及远程函数调用。
2. **事件驱动**：支持定时任务调度（Cron/Rate）、异步任务执行及响应各类 AWS 事件（如 S3 上传、DynamoDB 变更、SNS/SQS 消息等）。
3. **高级配置**：涵盖自定义域名与 SSL 证书（Let's Encrypt/ACM）、VPC 网络隔离、EFS 持久化存储、环境变量管理、IAM 权限控制及 WebSocket 支持。
4. **兼容性与优化**：兼容 Python 3.9+，支持 Docker 工作流、大型项目包优化（Slim Handler），并提供 Django 管理命令集成。