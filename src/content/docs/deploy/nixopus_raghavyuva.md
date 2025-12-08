
---
title: nixopus
---

### [raghavyuva nixopus](https://github.com/raghavyuva/nixopus)

**核心内容总结：**

Nixopus 是一个开源的替代 Vercel、Heroku、Netlify 的平台，支持终端集成和自托管功能。主要特性包括：一键部署应用（无需配置文件或 SSH 命令）、浏览器内管理文件、内置终端访问服务器、实时监控系统资源（CPU/内存/磁盘）、自动 SSL 证书、GitHub 集成自动部署、代理管理（Caddy 反向代理）、多渠道告警（Slack/Discord/邮件）。

**使用方法：**  
通过终端执行 `curl` 安装命令快速部署，支持自定义 IP、域名等参数。安装时需 root 权限（sudo），可选参数包括指定 API 域名、访问域名、超时时间等。当前为 alpha 预发布版本，不建议用于生产环境。